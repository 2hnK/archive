package com.devarchive.project;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Optional;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Service;

@Service
public class ProjectService {
	private final List<ProjectDraft> drafts = List.of(
			new ProjectDraft(
					"soomgil",
					"Soomgil",
					"스와이프 취향 데이터를 여행방 추천, 지도 일정 협업, 여행 기록 공유까지 연결한 그룹 여행 웹 앱",
					List.of(
							"Vue 3",
							"TypeScript",
							"Vite",
							"Pinia",
							"Mapbox GL JS",
							"Spring Boot",
							"Java 21",
							"PostgreSQL",
							"Redis",
							"MyBatis",
							"Flyway",
							"Spring AI",
							"STOMP WebSocket",
							"MinIO/S3",
							"Docker Compose"),
					"2026",
					"/images/projects/soomgil-trip-planning-cc0.jpg",
					"/videos/Soomgil-demo.mp4",
					"스와이프로 모은 개인 취향을 그룹 여행 계획, 지도 일정 편집, 여행 기록 공유까지 이어 붙인 서비스 개발 기록"),
			new ProjectDraft(
					"dyslexia-kit",
					"Dyslexia Kit",
					"학습 자료 PDF를 AI 활용해 난독증을 겪는 학생들을 위한 교안으로 변환하고, TTS·어휘 분석·쓰기 연습을 제공하는 서비스",
					List.of("Spring Boot", "React", "FastAPI", "LangChain", "PostgreSQL", "Redis", "AWS"),
					"2025",
					"/images/projects/dyslexia-kit-children-reading-public-domain.jpg",
					"/videos/dyslexia-kit-demo.mp4",
					"PDF 원문 교재를 AI로 분석하고 재구성해, 난독증 아동이 더 쉽게 읽고 이해할 수 있는 교안으로 변환하는 서비스의 개발 기록")
	);

	public List<Project> findAll() {
		return drafts.stream().map(this::toProject).toList();
	}

	public Optional<Project> findBySlug(String slug) {
		return drafts.stream()
				.filter(project -> project.slug().equals(slug))
				.findFirst()
				.map(this::toProject);
	}

	private Project toProject(ProjectDraft draft) {
		return new Project(
				draft.slug(),
				draft.title(),
				draft.description(),
				draft.tags(),
				draft.year(),
				draft.image(),
				draft.video(),
				draft.archivalNote(),
				readContent(draft.slug()));
	}

	private String readContent(String slug) {
		ClassPathResource resource = new ClassPathResource("content/projects/" + slug + ".html");
		if (!resource.exists()) {
			return "";
		}
		try {
			return new String(resource.getInputStream().readAllBytes(), StandardCharsets.UTF_8);
		} catch (IOException ex) {
			throw new UncheckedIOException("프로젝트 본문을 읽을 수 없습니다: " + slug, ex);
		}
	}

	private record ProjectDraft(
			String slug,
			String title,
			String description,
			List<String> tags,
			String year,
			String image,
			String video,
			String archivalNote
	) {
	}
}
