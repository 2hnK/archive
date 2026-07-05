---
type: Documentation Policy
title: OKF 문서 형식
description: DevArchive 문서를 Open Knowledge Format 기반 지식 단위로 관리하는 규칙.
tags: ["documentation", "okf", "agent-context"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# OKF 문서 형식

## 목적

DevArchive의 문서는 에이전트와 사람이 함께 읽는 버전 관리 지식 베이스다. Google Cloud의 Open Knowledge Format(OKF)은 Markdown과 YAML frontmatter만으로 지식 단위를 표현하므로, 현재 `docs/` 중심 구조에 큰 런타임을 추가하지 않고 적용할 수 있다.

## 적용 판단

OKF 적용은 도움이 된다. 이 저장소의 문서는 이미 작은 주제별 Markdown으로 나뉘어 있고, Git diff로 변경 내역을 검토하며, `AGENTS.md`가 문서 지도를 제공한다. OKF frontmatter를 추가하면 각 문서의 성격을 기계적으로 식별할 수 있어 에이전트가 문서 탐색과 검증을 더 안정적으로 수행할 수 있다.

다만 OKF v0.1은 draft이므로 이 프로젝트에서는 최소 호환 규칙만 채택한다.

## 적용 범위

- Git이 추적하는 Markdown 파일은 OKF concept document로 취급한다.
- `README.md`, `AGENTS.md`, `docs/**/*.md`, `src/content/articles/**/*.md`는 `type` 필드를 가진 YAML frontmatter를 둔다.
- `node_modules/`, `dist/`, `.astro/`, `.dump/`는 문서 검증 대상이 아니다.
- `.dump/`는 `.gitignore`에 포함된 로컬 초안 영역이므로 OKF 변환 대상에서 제외한다.

## Frontmatter 규칙

필수 필드:

- `type`: 문서의 지식 유형. 예: `Project Index`, `Development Guide`, `Design Reference`, `Article`

권장 필드:

- `title`: 사람이 읽는 표시 이름
- `description`: 한 문장 요약
- `tags`: 검색과 분류를 위한 짧은 문자열 배열
- `timestamp`: 의미 있는 마지막 문서 정비 시점의 ISO 8601 문자열

## 작성 규칙

- 본문은 일반 Markdown을 유지한다.
- 큰 문서 하나에 모든 정책을 넣지 않고, 주제별 문서로 나눈다.
- 문서 간 관계는 상대 Markdown 링크로 연결한다.
- 새 정책이나 중요한 판단은 `docs/decisions/`에 결정 기록으로 남긴다.
- 프런트매터 필드를 추가해도 Astro 콘텐츠 스키마와 빌드가 깨지지 않는지 `npm run verify`로 확인한다.

## 검증

문서 검증은 `scripts/validate-docs.mjs`가 수행한다.

```sh
npm run docs:validate
```

검증 항목:

- 모든 추적 Markdown 파일에 OKF frontmatter가 있는지 확인
- `type` 필드가 비어 있지 않은지 확인
- `tags`와 `timestamp` 형식 확인
- 로컬 Markdown/이미지 링크가 실제 파일을 가리키는지 확인

