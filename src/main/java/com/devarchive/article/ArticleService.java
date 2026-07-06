package com.devarchive.article;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.charset.StandardCharsets;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Optional;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.commonmark.Extension;
import org.commonmark.ext.gfm.tables.TablesExtension;
import org.commonmark.node.AbstractVisitor;
import org.commonmark.node.Code;
import org.commonmark.node.Heading;
import org.commonmark.node.Node;
import org.commonmark.node.SoftLineBreak;
import org.commonmark.node.Text;
import org.commonmark.parser.Parser;
import org.commonmark.renderer.html.HtmlRenderer;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.ResourcePatternResolver;
import org.springframework.stereotype.Service;

@Service
public class ArticleService {
	private static final Pattern FRONTMATTER = Pattern.compile("\\A---\\R([\\s\\S]*?)\\R---\\R?");

	private final ResourcePatternResolver resourcePatternResolver;
	private final Parser parser;
	private final HtmlRenderer htmlRenderer;
	private volatile List<Article> cache;

	public ArticleService(ResourcePatternResolver resourcePatternResolver) {
		List<Extension> extensions = List.of(TablesExtension.create());
		this.resourcePatternResolver = resourcePatternResolver;
		this.parser = Parser.builder().extensions(extensions).build();
		this.htmlRenderer = HtmlRenderer.builder().extensions(extensions).escapeHtml(false).build();
	}

	public List<Article> findAll() {
		List<Article> current = cache;
		if (current == null) {
			current = loadArticles();
			cache = current;
		}
		return current;
	}

	public List<Article> findLatest(int count) {
		return findAll().stream().limit(count).toList();
	}

	public Optional<Article> findBySlug(String slug) {
		return findAll().stream().filter(article -> article.slug().equals(slug)).findFirst();
	}

	public List<TopicCategory> findTopics() {
		Map<String, MutableTopic> topics = new LinkedHashMap<>();
		for (Article article : findAll()) {
			MutableTopic topic = topics.computeIfAbsent(article.category(), ignored -> new MutableTopic());
			topic.count++;
			if (article.subcategory() != null && !article.subcategory().isBlank()) {
				topic.subCounts.merge(article.subcategory(), 1, Integer::sum);
			}
		}
		return topics.entrySet().stream()
				.sorted(Map.Entry.comparingByKey())
				.map(entry -> new TopicCategory(
						entry.getKey(),
						entry.getValue().count,
						entry.getValue().subCounts.entrySet().stream()
								.sorted(Map.Entry.comparingByKey())
								.map(sub -> new TopicSubcategory(sub.getKey(), sub.getValue()))
								.toList()))
				.toList();
	}

	public int count() {
		return findAll().size();
	}

	private List<Article> loadArticles() {
		try {
			Resource[] resources = resourcePatternResolver.getResources("classpath:/content/articles/*.md");
			List<Article> articles = new ArrayList<>();
			for (Resource resource : resources) {
				articles.add(loadArticle(resource));
			}
			articles.sort(Comparator.comparing(Article::date).reversed());
			return List.copyOf(articles);
		} catch (IOException ex) {
			throw new UncheckedIOException("아티클 콘텐츠를 읽을 수 없습니다.", ex);
		}
	}

	private Article loadArticle(Resource resource) throws IOException {
		String filename = resource.getFilename();
		if (filename == null || !filename.endsWith(".md")) {
			throw new IllegalArgumentException("지원하지 않는 아티클 파일입니다: " + resource);
		}
		String slug = filename.substring(0, filename.length() - 3);
		String raw = new String(resource.getInputStream().readAllBytes(), StandardCharsets.UTF_8);
		ParsedMarkdown parsed = splitFrontmatter(raw);
		Map<String, String> meta = parseYamlLikeFrontmatter(parsed.frontmatter());

		Node document = parser.parse(parsed.body());
		List<com.devarchive.article.Heading> headings = extractHeadings(document);
		String html = postProcessHtml(htmlRenderer.render(document), headings);

		return new Article(
				slug,
				meta.getOrDefault("title", slug),
				meta.getOrDefault("description", ""),
				meta.getOrDefault("category", "General"),
				blankToNull(meta.get("subcategory")),
				LocalDate.parse(meta.getOrDefault("date", "1970-01-01")),
				meta.getOrDefault("timestamp", ""),
				blankToNull(meta.get("imageUrl")),
				Boolean.parseBoolean(meta.getOrDefault("isFeatured", "false")),
				parsed.body(),
				html,
				toSnippet(parsed.body()),
				headings);
	}

	private ParsedMarkdown splitFrontmatter(String raw) {
		Matcher matcher = FRONTMATTER.matcher(raw);
		if (!matcher.find()) {
			return new ParsedMarkdown("", raw);
		}
		return new ParsedMarkdown(matcher.group(1), raw.substring(matcher.end()));
	}

	private Map<String, String> parseYamlLikeFrontmatter(String source) {
		Map<String, String> values = new HashMap<>();
		for (String line : source.split("\\R")) {
			if (line.isBlank() || line.trim().startsWith("#")) {
				continue;
			}
			String[] parts = line.split(":", 2);
			if (parts.length != 2) {
				continue;
			}
			values.put(parts[0].trim(), unquote(parts[1].trim()));
		}
		return values;
	}

	private String unquote(String value) {
		if ((value.startsWith("\"") && value.endsWith("\""))
				|| (value.startsWith("'") && value.endsWith("'"))) {
			return value.substring(1, value.length() - 1);
		}
		return value;
	}

	private List<com.devarchive.article.Heading> extractHeadings(Node document) {
		List<com.devarchive.article.Heading> headings = new ArrayList<>();
		Map<String, Integer> duplicateTracker = new HashMap<>();
		document.accept(new AbstractVisitor() {
			@Override
			public void visit(Heading heading) {
				String text = collectText(heading).trim();
				String slug = uniqueSlug(text, duplicateTracker);
				headings.add(new com.devarchive.article.Heading(heading.getLevel(), text, slug));
				visitChildren(heading);
			}
		});
		return List.copyOf(headings);
	}

	private String collectText(Node node) {
		StringBuilder builder = new StringBuilder();
		node.accept(new AbstractVisitor() {
			@Override
			public void visit(Text text) {
				builder.append(text.getLiteral());
			}

			@Override
			public void visit(Code code) {
				builder.append(code.getLiteral());
			}

			@Override
			public void visit(SoftLineBreak softLineBreak) {
				builder.append(' ');
			}
		});
		return builder.toString();
	}

	private String uniqueSlug(String text, Map<String, Integer> duplicateTracker) {
		String base = text.toLowerCase(Locale.ROOT)
				.replaceAll("[^\\p{IsAlphabetic}\\p{IsDigit}\\p{IsHangul}]+", "-")
				.replaceAll("(^-|-$)", "");
		if (base.isBlank()) {
			base = "section";
		}
		int count = duplicateTracker.merge(base, 1, Integer::sum);
		return count == 1 ? base : base + "-" + count;
	}

	private String postProcessHtml(String html, List<com.devarchive.article.Heading> headings) {
		Document document = Jsoup.parseBodyFragment(html);
		List<Element> headingElements = document.select("h1,h2,h3,h4,h5,h6");
		for (int i = 0; i < headingElements.size() && i < headings.size(); i++) {
			headingElements.get(i).attr("id", headings.get(i).slug());
		}
		for (Element image : document.select("img[src]")) {
			String src = image.attr("src");
			if (src.startsWith("./images/")) {
				image.attr("src", "/content/articles/" + src.substring(2));
			}
		}
		return document.body().html();
	}

	private String toSnippet(String markdown) {
		String text = markdown
				.replaceAll("(?s)```.*?```", " ")
				.replaceAll("!\\[[^]]*]\\([^)]+\\)", " ")
				.replaceAll("\\[([^]]+)]\\([^)]+\\)", "$1")
				.replaceAll("`([^`]*)`", "$1")
				.replaceAll("<[^>]+>", " ")
				.replaceAll("[*_#>\\-]+", " ")
				.replaceAll("\\s+", " ")
				.trim();
		return text.length() > 500 ? text.substring(0, 500) + "..." : text;
	}

	private String blankToNull(String value) {
		return value == null || value.isBlank() ? null : value;
	}

	private record ParsedMarkdown(String frontmatter, String body) {
	}

	private static final class MutableTopic {
		private int count;
		private final Map<String, Integer> subCounts = new LinkedHashMap<>();
	}
}
