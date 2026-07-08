---
type: Backend Implementation Guide
title: Spring SSR Implementation Guide
description: DevArchive DB 기반 SSR 구현을 위한 Spring MVC, JPA, Thymeleaf 실습 가이드.
tags: ["backend", "spring-mvc", "jpa", "thymeleaf"]
timestamp: "2026-07-09T00:00:00+09:00"
---

# Spring SSR Implementation Guide

## 목적

이 문서는 DevArchive를 직접 구현하면서 Spring MVC, JPA, Thymeleaf 폼 처리를 익히기 위한 구현 가이드다. 완성 코드를 복사하는 문서가 아니라, 현재 구조에서 어떤 책임을 어디에 둘지 판단하는 기준을 제공한다.

## SSR 요청 흐름

기본 흐름:

```text
브라우저 요청
  -> Controller
  -> Service
  -> Repository
  -> Database
  -> Model
  -> Thymeleaf template
  -> HTML 응답
```

예시:

```text
GET /articles/wireshark-lab-dns
  -> SiteController.article(slug, model)
  -> ArticleService.findBySlug(slug)
  -> ArticleRepository.findBySlug(slug)
  -> model.addAttribute("article", article)
  -> return "articles/detail"
```

## 레이어별 책임

### Controller

역할:

- URL과 HTTP method를 받는다.
- 요청 파라미터, path variable, form 데이터를 받는다.
- Service를 호출한다.
- Thymeleaf에 넘길 Model을 구성한다.
- 어떤 template을 렌더링할지 결정한다.

Controller에 두지 않을 것:

- DB 직접 조회
- 복잡한 비즈니스 규칙
- 긴 Markdown/HTML 변환 로직
- Entity 생성 세부 규칙

### Service

역할:

- 기능의 흐름을 조립한다.
- Repository를 호출한다.
- 없는 데이터, 중복 slug, 상태값 같은 규칙을 처리한다.
- Entity를 화면용 객체로 변환한다.
- 트랜잭션 경계를 잡는다.

처음에는 현재 `ArticleService` 메서드 이름을 유지하는 것이 좋다.

```text
findAll()
findLatest(int limit)
findBySlug(String slug)
findTopics()
count()
```

이렇게 하면 Controller와 template 변경을 줄이고, 내부 구현만 파일 조회에서 DB 조회로 바꿀 수 있다.

### Repository

역할:

- DB 조회와 저장을 담당한다.
- Spring Data JPA의 메서드 이름 쿼리로 시작한다.
- 복잡한 조회가 필요해지면 `@Query`나 QueryDSL을 검토한다.

초기 예시:

```java
public interface ArticleRepository extends JpaRepository<ArticleEntity, Long> {
    Optional<ArticleEntity> findBySlug(String slug);
    boolean existsBySlug(String slug);
    List<ArticleEntity> findAllByStatusOrderByPublishedAtDesc(ArticleStatus status);
}
```

## Entity 작성 기준

Entity는 DB 테이블과 가까운 객체다.

기본 원칙:

- `id`는 surrogate key로 둔다.
- URL 식별자는 `slug`로 둔다.
- `slug`에는 unique 제약을 둔다.
- 생성/수정 시간은 공통 필드로 관리한다.
- 화면 출력 포맷은 Entity 안에 과하게 넣지 않는다.

초기 Article Entity 후보:

```java
@Entity
@Table(name = "articles")
public class ArticleEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true, length = 160)
    private String slug;

    @Column(nullable = false, length = 200)
    private String title;

    @Column(nullable = false, length = 500)
    private String description;

    @Lob
    @Column(nullable = false)
    private String contentMarkdown;
}
```

학습 포인트:

- `@Column(nullable = false)`와 DB `NOT NULL`의 관계
- `unique = true`와 중복 slug 처리
- `@Lob` 사용 시 DB별 실제 타입 차이
- `LocalDateTime`과 화면 날짜 포맷 분리

## DB와 Migration 기준

이 프로젝트의 DB 기반 콘텐츠 전환은 PostgreSQL과 Flyway를 기준으로 한다.

권장 시작 순서:

1. `build.gradle`에 PostgreSQL JDBC driver와 Flyway 의존성을 추가한다.
2. 로컬 PostgreSQL을 Docker로 실행한다.
3. `src/main/resources/db/migration/V1__create_articles.sql`부터 작성한다.
4. 애플리케이션 시작 시 Flyway migration이 적용되는지 확인한다.
5. JPA Entity는 migration schema와 이름/타입을 맞춘다.

주의할 점:

- 이미 적용한 Flyway migration 파일은 수정하지 않는다.
- schema 변경은 `V2__...sql`, `V3__...sql`처럼 새 파일로 추가한다.
- `spring.jpa.hibernate.ddl-auto=create`에 의존하지 않는다. 학습 초반에도 schema의 기준은 migration 파일로 둔다.
- 테스트 편의를 위해 H2를 쓰더라도, 운영 기준 SQL은 PostgreSQL을 기준으로 검토한다.

## 본문 렌더링 기준

Article 본문은 `content_markdown`을 원본으로 저장한다.

처음 구현:

```text
DB content_markdown
  -> ArticleService
  -> Markdown renderer
  -> ArticleDetail.html
  -> Thymeleaf
```

나중에 캐시가 필요해지면 다음 구조로 확장한다.

```text
글 저장/수정 시 content_html 생성
글 조회 시 content_html이 있으면 사용
content_html이 없으면 content_markdown을 변환
```

이 구조를 쓰는 이유:

- 작성/수정 화면에서 원본 Markdown을 그대로 보여줄 수 있다.
- 렌더링 정책을 바꿔도 원본에서 다시 HTML을 생성할 수 있다.
- HTML 캐시는 성능 최적화가 필요할 때만 도입할 수 있다.

## 이미지와 Object Storage 기준

이미지와 영상 바이너리는 DB에 저장하지 않는다. DB에는 public URL 또는 object key만 저장한다.

로컬 개발 기준:

```text
Docker MinIO
  -> bucket: devarchive
  -> object key: articles/{slug}/{fileName}
  -> DB image_object_key 또는 image_url 저장
```

로컬 MinIO 예시:

```yaml
services:
  minio:
    image: minio/minio:latest
    command: server /data --console-address ":9001"
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: devarchive
      MINIO_ROOT_PASSWORD: devarchive-password
    volumes:
      - minio-data:/data

volumes:
  minio-data:
```

외부 스토리지를 쓰는 이유:

- DB 백업과 migration이 이미지/영상 파일 크기에 끌려가지 않는다.
- 파일 제공 책임을 애플리케이션 서버와 분리할 수 있다.
- CDN 또는 S3 호환 저장소로 확장하기 쉽다.
- AWS를 쓰지 않아도 MinIO, Cloudflare R2, Naver Object Storage처럼 S3 호환 API를 기준으로 연습할 수 있다.

초기 구현에서는 업로드 기능보다 먼저 `image_url` 문자열 저장과 표시를 구현한다. 이후 업로드 기능을 붙일 때 `StorageService`를 만들고 MinIO/S3 SDK 호출을 캡슐화한다.

## DTO 사용 기준

초기에는 Entity를 template에 직접 넘겨도 학습은 가능하다. 다만 다음 상황이 오면 DTO를 만든다.

- 화면에서 필요한 필드와 Entity 필드가 달라진다.
- 날짜 포맷, snippet, URL 같은 화면용 값이 많아진다.
- Entity 관계가 template에서 지연 로딩 문제를 만든다.
- 작성 폼과 DB Entity 구조가 다르다.

권장 DTO 종류:

- `ArticleListItem`
- `ArticleDetail`
- `ArticleForm`
- `ProjectListItem`
- `ProjectDetail`

## Thymeleaf 목록/상세 처리

Controller는 기존 model key를 유지하는 편이 좋다.

```java
model.addAttribute("articles", articleService.findAll());
model.addAttribute("topics", articleService.findTopics());
```

템플릿은 이미 `articles`, `article`, `topics` 같은 이름에 의존한다. DB 전환 때 이 이름을 유지하면 화면 변경을 줄일 수 있다.

## Thymeleaf 폼 처리

작성 화면 기본 흐름:

```text
GET /write
  -> 빈 ArticleForm을 model에 추가
  -> write.html 렌더링

POST /articles
  -> ArticleForm 바인딩
  -> validation
  -> Service 저장
  -> redirect:/articles/{slug}
```

폼 객체 예시:

```java
public class ArticleForm {
    @NotBlank
    private String title;

    @NotBlank
    private String slug;

    @NotBlank
    private String description;

    @NotBlank
    private String contentMarkdown;
}
```

Controller 예시 흐름:

```java
@PostMapping("/articles")
public String createArticle(
        @Valid @ModelAttribute("articleForm") ArticleForm form,
        BindingResult bindingResult
) {
    if (bindingResult.hasErrors()) {
        return "write";
    }

    ArticleDetail article = articleService.create(form);
    return "redirect:/articles/" + article.slug();
}
```

중요한 규칙:

- `BindingResult`는 `@Valid`가 붙은 파라미터 바로 뒤에 둔다.
- validation 실패 시 redirect하지 않고 원래 template을 다시 렌더링한다.
- 저장 성공 시에는 refresh 중복 제출을 막기 위해 redirect한다.

## Validation 기준

Article 작성의 최소 검증:

- title 필수
- slug 필수
- slug 형식: 영문 소문자, 숫자, 하이픈
- slug unique
- description 필수
- contentMarkdown 필수
- category 선택 여부

slug 형식 예시:

```text
^[a-z0-9]+(?:-[a-z0-9]+)*$
```

## 예외 처리 기준

초기에는 Controller에서 다음 패턴을 유지해도 된다.

```java
articleService.findBySlug(slug)
    .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND));
```

기능이 늘어나면 다음으로 확장한다.

- `ArticleNotFoundException`
- `DuplicateSlugException`
- `@ControllerAdvice`
- 에러 페이지 template

## 트랜잭션 기준

조회:

```java
@Transactional(readOnly = true)
```

쓰기:

```java
@Transactional
```

Service 메서드에 붙이는 것을 기본으로 한다. Controller나 Repository에 트랜잭션 흐름을 흩뿌리지 않는다.

## 구현 순서 추천

1. Article 목록 DB 조회
2. Article 상세 DB 조회
3. 없는 slug 404
4. Article 작성 폼 저장
5. validation 에러 화면 표시
6. Article 수정
7. Article archive/delete
8. 이미지 URL 저장과 표시
9. MinIO 업로드 연동
10. Category 관계
11. Tag 관계
12. Project DB 조회

## 구현할 때 지킬 것

- 처음부터 모든 관계를 만들지 않는다.
- Article 단일 테이블 조회부터 끝낸다.
- Service 메서드 시그니처는 가능한 한 기존 구조와 맞춘다.
- template model key를 쉽게 바꾸지 않는다.
- DB 이관 전후로 URL은 유지한다.
- 막히는 에러는 [트러블슈팅](05-troubleshooting.md)에 증상과 해결 순서를 기록한다.
