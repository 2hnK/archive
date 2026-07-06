package com.devarchive.web;

import com.devarchive.article.ArticleService;
import com.devarchive.project.ProjectService;
import java.util.List;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.server.ResponseStatusException;

@Controller
public class SiteController {
	private final ArticleService articleService;
	private final ProjectService projectService;

	public SiteController(ArticleService articleService, ProjectService projectService) {
		this.articleService = articleService;
		this.projectService = projectService;
	}

	@GetMapping("/")
	public String home(Model model) {
		model.addAttribute("title", "DEVARCHIVE");
		model.addAttribute("description", "Artistic Dev Blog");
		model.addAttribute("latestArticles", articleService.findLatest(5));
		model.addAttribute("projects", projectService.findAll());
		return "index";
	}

	@GetMapping("/articles")
	public String articles(
			@RequestParam(required = false) String cat,
			@RequestParam(required = false) String sub,
			Model model
	) {
		model.addAttribute("title", "Articles | DEVARCHIVE");
		model.addAttribute("description", "모든 아티클 및 저널 목록입니다.");
		model.addAttribute("articles", articleService.findAll());
		model.addAttribute("topics", articleService.findTopics());
		model.addAttribute("articleCount", articleService.count());
		model.addAttribute("currentCat", cat);
		model.addAttribute("currentSub", sub);
		return "articles/index";
	}

	@GetMapping("/articles/{slug}")
	public String article(@PathVariable String slug, Model model) {
		var article = articleService.findBySlug(slug)
				.orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND));
		model.addAttribute("title", article.title() + " | DEVARCHIVE");
		model.addAttribute("description", article.description());
		model.addAttribute("article", article);
		model.addAttribute("topics", articleService.findTopics());
		model.addAttribute("articleCount", articleService.count());
		model.addAttribute("currentCat", article.category());
		model.addAttribute("currentSub", article.subcategory());
		return "articles/detail";
	}

	@GetMapping("/project")
	public String projects(Model model) {
		model.addAttribute("title", "Works | DEVARCHIVE");
		model.addAttribute("description", "Selected Projects");
		model.addAttribute("projects", projectService.findAll());
		return "project/index";
	}

	@GetMapping("/project/{slug}")
	public String project(@PathVariable String slug, Model model) {
		var project = projectService.findBySlug(slug)
				.orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND));
		model.addAttribute("title", project.title() + " | DEVARCHIVE");
		model.addAttribute("description", project.description());
		model.addAttribute("project", project);
		return "project/detail";
	}

	@GetMapping("/about")
	public String about(Model model) {
		model.addAttribute("title", "About | DEVARCHIVE");
		model.addAttribute("description", "Dynamic Spatial About Page");
		model.addAttribute("timeline", timeline());
		model.addAttribute("certifications", certifications());
		model.addAttribute("skills", skills());
		return "about";
	}

	@GetMapping("/snippets")
	public String snippets(Model model) {
		model.addAttribute("title", "Snippets | DevArchive");
		model.addAttribute("description", "유용한 코드 조각 및 실험실");
		model.addAttribute("snippets", snippetsData());
		return "snippets";
	}

	@GetMapping("/write")
	public String write(Model model) {
		model.addAttribute("title", "Write | DevArchive");
		model.addAttribute("description", "블로그 포스트 작성 에디터");
		return "write";
	}

	@GetMapping("/write-project")
	public String writeProject(Model model) {
		model.addAttribute("title", "New Project | DevArchive");
		model.addAttribute("description", "프로젝트 카드 생성 에디터");
		return "write-project";
	}

	private List<Milestone> timeline() {
		return List.of(
				new Milestone(
						"2026.01 ~ 현재",
						"삼성청년SW/AI아카데미(SSAFY)",
						"체계적인 실무 중심의 교육을 통해 웹 개발 및 AI 활용 능력 역량 강화 및 알고리즘 문제 해결 능력 향상",
						"/assets/ssafy_logo.svg",
						null),
				new Milestone(
						"2024.03 ~ 2026.02",
						"국립한밭대학교 컴퓨터공학 학사 졸업",
						"자료구조, 알고리즘 등 컴퓨터공학 전공 과정을 통해 소프트웨어 엔지니어링의 기본 소양 확립",
						"/assets/hanbat_logo.svg",
						null),
				new Milestone(
						"2026.02",
						"KICS 동계종합학술발표회",
						"KICS 한국통신학회 · 2026년도 동계종합학술발표회(KICS Winter Conference 2026) - 비용효율적인 지능형 AICC를 위한 자가진화형 4계층 정규화 게이트",
						"/assets/kics_logo.jpg",
						"장려상"));
	}

	private List<Certification> certifications() {
		return List.of(
				new Certification("정보처리기사", "2025.09", "한국산업인력공단", "/assets/engineer_information_processing_logo.png"),
				new Certification("SQLD", "2025.06", "한국데이터산업진흥원", "/assets/sqld_logo.png"));
	}

	private List<Skill> skills() {
		return List.of(
				new Skill("Java", "https://cdn.simpleicons.org/openjdk"),
				new Skill("Python", "https://cdn.simpleicons.org/python"),
				new Skill("Spring", "https://cdn.simpleicons.org/spring"),
				new Skill("Spring AI", "https://cdn.simpleicons.org/spring"),
				new Skill("LangChain", "https://cdn.simpleicons.org/langchain"),
				new Skill("MySQL", "https://cdn.simpleicons.org/mysql"),
				new Skill("PostgreSQL", "https://cdn.simpleicons.org/postgresql"),
				new Skill("Redis", "https://cdn.simpleicons.org/redis"),
				new Skill("Docker", "https://cdn.simpleicons.org/docker"),
				new Skill("AWS", "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg"));
	}

	private List<Snippet> snippetsData() {
		return List.of(
				new Snippet(
						"Centering a Div",
						"가장 클래식한 문제. Flexbox를 활용한 완벽한 뷰포트 정중앙 정렬.",
						".container {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  height: 100vh;\n}",
						"css",
						"CSS"),
				new Snippet(
						"Random UUID in Browser",
						"외부 라이브러리 의존성 없이 브라우저 내장 API를 활용해 UUIDv4를 생성하는 깔끔한 방법.",
						"const uuid = () => crypto.randomUUID();",
						"javascript",
						"JS"),
				new Snippet(
						"React useEffect Cleanup",
						"타이머나 이벤트 리스너를 붙일 때 메모리 누수를 방지하기 위해 잊지 말아야 할 클린업 패턴.",
						"useEffect(() => {\n  const timer = setInterval(() => {\n    console.log('tick');\n  }, 1000);\n\n  return () => clearInterval(timer);\n}, []);",
						"javascript",
						"React"),
				new Snippet(
						"Spring MVC 정적 라우팅",
						"Thymeleaf SSR에서 간단한 화면 라우트를 컨트롤러 메서드로 연결하는 패턴입니다.",
						"@GetMapping(\"/articles/{slug}\")\npublic String article(@PathVariable String slug, Model model) {\n  model.addAttribute(\"article\", service.findBySlug(slug));\n  return \"articles/detail\";\n}",
						"java",
						"Spring"),
				new Snippet(
						"Tailwind Glassmorphism",
						"자주 쓰는 글래스모피즘 느낌의 Tailwind 유틸리티 클래스 조합.",
						"bg-white/10 backdrop-blur-md border border-white/20 shadow-xl",
						"css",
						"Tailwind"),
				new Snippet(
						"Debounce Function",
						"연속된 이벤트 호출 시 마지막 호출만 실행되도록 제어하는 디바운스 유틸리티 함수.",
						"function debounce(func, wait) {\n  let timeout;\n  return function executedFunction(...args) {\n    clearTimeout(timeout);\n    timeout = setTimeout(() => func(...args), wait);\n  };\n}",
						"javascript",
						"TS"));
	}
}
