import { existsSync, readFileSync } from "node:fs";
import { dirname, extname, isAbsolute, normalize, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import YAML from "yaml";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");

const gitResult = spawnSync("git", ["ls-files", "--cached", "--others", "--exclude-standard", "*.md"], {
  cwd: root,
  encoding: "utf8",
});

if (gitResult.status !== 0) {
  console.error("git ls-files 실행에 실패했습니다.");
  process.exit(1);
}

const docs = gitResult.stdout
  .split(/\r?\n/)
  .map((file) => file.trim())
  .filter(Boolean)
  .filter((file) => !file.startsWith("node_modules/"));

const errors = [];

for (const relativePath of docs) {
  const absolutePath = resolve(root, relativePath);
  const content = readFileSync(absolutePath, "utf8");
  const frontmatter = parseFrontmatter(content, relativePath);

  if (!frontmatter) {
    errors.push(`${relativePath}: OKF frontmatter가 없습니다.`);
  } else {
    validateFrontmatter(relativePath, frontmatter);
  }

  validateLocalLinks(relativePath, content);
}

if (errors.length > 0) {
  console.error("문서 검증 실패:");
  for (const error of errors) {
    console.error(`- ${error}`);
  }
  process.exit(1);
}

console.log(`문서 검증 완료: ${docs.length}개 Markdown 파일`);

function parseFrontmatter(content, relativePath) {
  if (!content.startsWith("---\n") && !content.startsWith("---\r\n")) {
    return null;
  }

  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/);
  if (!match) {
    errors.push(`${relativePath}: frontmatter 닫힘 구분자(---)가 없습니다.`);
    return null;
  }

  try {
    const data = YAML.parse(match[1]);
    if (!data || typeof data !== "object" || Array.isArray(data)) {
      errors.push(`${relativePath}: frontmatter는 YAML 객체여야 합니다.`);
      return null;
    }
    return data;
  } catch (error) {
    errors.push(`${relativePath}: YAML 파싱 실패 - ${error.message}`);
    return null;
  }
}

function validateFrontmatter(relativePath, frontmatter) {
  if (typeof frontmatter.type !== "string" || frontmatter.type.trim() === "") {
    errors.push(`${relativePath}: OKF 필수 필드 type이 필요합니다.`);
  }

  for (const field of ["title", "description", "resource", "timestamp"]) {
    if (
      Object.hasOwn(frontmatter, field) &&
      frontmatter[field] !== null &&
      typeof frontmatter[field] !== "string"
    ) {
      errors.push(`${relativePath}: ${field} 필드는 문자열이어야 합니다.`);
    }
  }

  if (
    typeof frontmatter.timestamp === "string" &&
    Number.isNaN(Date.parse(frontmatter.timestamp))
  ) {
    errors.push(`${relativePath}: timestamp는 ISO 8601 날짜/시간이어야 합니다.`);
  }

  if (
    Object.hasOwn(frontmatter, "tags") &&
    (!Array.isArray(frontmatter.tags) ||
      frontmatter.tags.some((tag) => typeof tag !== "string" || tag.trim() === ""))
  ) {
    errors.push(`${relativePath}: tags 필드는 문자열 배열이어야 합니다.`);
  }
}

function validateLocalLinks(relativePath, content) {
  const linkPattern = /!?\[[^\]]*]\(([^)\s]+)(?:\s+"[^"]*")?\)/g;
  let match;

  while ((match = linkPattern.exec(content)) !== null) {
    const rawHref = match[1].trim();
    const hrefWithoutAnchor = rawHref.split("#")[0];

    if (!hrefWithoutAnchor || shouldSkipHref(hrefWithoutAnchor)) {
      continue;
    }

    const decodedHref = decodeURIComponentSafe(hrefWithoutAnchor);
    const target = resolveLinkTarget(relativePath, decodedHref);

    if (!existsSync(target)) {
      errors.push(`${relativePath}: 깨진 로컬 링크 - ${rawHref}`);
      continue;
    }

    if (extname(target).toLowerCase() === ".md" && !isTrackedMarkdown(target)) {
      errors.push(`${relativePath}: 추적되지 않는 Markdown 링크 - ${rawHref}`);
    }
  }
}

function shouldSkipHref(href) {
  return (
    href.startsWith("http://") ||
    href.startsWith("https://") ||
    href.startsWith("mailto:") ||
    href.startsWith("tel:") ||
    href.startsWith("data:") ||
    href.startsWith("javascript:")
  );
}

function decodeURIComponentSafe(value) {
  try {
    return decodeURIComponent(value);
  } catch {
    return value;
  }
}

function resolveLinkTarget(relativePath, href) {
  if (href.startsWith("/")) {
    return resolve(root, href.slice(1));
  }

  if (isAbsolute(href)) {
    return normalize(href);
  }

  return resolve(root, dirname(relativePath), href);
}

function isTrackedMarkdown(target) {
  const normalizedTarget = normalize(target);
  return docs.some((file) => normalize(resolve(root, file)) === normalizedTarget);
}
