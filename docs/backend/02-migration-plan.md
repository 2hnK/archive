---
type: Backend Migration Plan
title: Static Content To DB Migration Plan
description: DevArchive 정적 콘텐츠를 DB 기반 조회 구조로 옮기기 위한 단계별 이관 계획서.
tags: ["backend", "migration", "roadmap", "checklist"]
timestamp: "2026-07-09T00:00:00+09:00"
---

# Static Content To DB Migration Plan

## 목적

이 문서는 현재 정적 파일/하드코딩 데이터로 동작하는 DevArchive를 DB 기반 SSR 구조로 바꾸기 위한 구현 로드맵이다.

핵심 원칙은 화면을 한 번에 갈아엎지 않는 것이다. 기존 Controller와 Thymeleaf 템플릿을 최대한 유지하고, Service가 데이터를 가져오는 출처를 파일/하드코딩에서 DB Repository로 점진적으로 바꾼다.

## 현재 데이터 출처

| 데이터 | 현재 위치 | 현재 담당 코드 | 이관 우선순위 |
| --- | --- | --- | --- |
| Article metadata/body | `src/main/resources/content/articles/*.md` | `ArticleService` | 높음 |
| Article image | `src/main/resources/static/content/articles/images/` | `ArticleService` HTML 후처리 | 높음 |
| Article topic/category | Markdown frontmatter | `ArticleService.findTopics()` | 중간 |
| Project metadata | `ProjectService` 하드코딩 | `ProjectService` | 중간 |
| Project detail | `src/main/resources/content/projects/*.html` | `ProjectService` | 중간 |
| Snippet | `SiteController.snippetsData()` | `SiteController` | 낮음 |
| About timeline/certification/skill | `SiteController` 하드코딩 | `SiteController` | 낮음 |

## 목표 구조

```text
Controller
  -> Service
  -> Repository
  -> Database
  -> DTO 또는 Entity
  -> Thymeleaf Model
  -> HTML 응답
```

컨트롤러의 라우트는 가능한 한 유지한다.

```text
/articles
/articles/{slug}
/project
/project/{slug}
/snippets
```

## 단계별 로드맵

### 0단계: DB 선택과 실행 환경 정하기

확정한 기준:

- 메인 DB는 PostgreSQL을 사용한다.
- schema 변경 이력은 Flyway로 관리한다.
- 로컬 객체 스토리지는 MinIO Docker 컨테이너를 사용한다.
- 테스트 DB는 초기 난이도에 따라 H2 또는 Testcontainers PostgreSQL 중 선택한다.

권장 학습 순서:

1. PostgreSQL Docker 컨테이너 실행 방법 정리
2. MinIO Docker 컨테이너 실행 방법 정리
3. `application.properties` 또는 profile 설정
4. Flyway `V1__...sql` migration 작성
5. 빈 DB 연결 확인
6. MinIO bucket 생성 확인

완료 조건:

- Spring Boot 실행 시 DB 연결 오류가 없다.
- Flyway migration이 성공한다.
- 빈 Repository 테스트 또는 간단한 health 확인이 가능하다.
- MinIO 콘솔에 접속하고 bucket을 만들 수 있다.

### 1단계: Article 조회를 DB로 교체

작업:

- `ArticleEntity` 작성
- `ArticleRepository` 작성
- Flyway seed 또는 별도 import 로직으로 초기 데이터 insert
- `ArticleService.findAll()`, `findLatest()`, `findBySlug()` 내부 조회를 DB로 변경
- `content_markdown` 원본을 저장하고 Service에서 HTML로 변환
- `image_url` 또는 `image_object_key`를 저장하고 본문 이미지 경로가 깨지지 않게 처리

처음에는 Markdown 파싱 기능을 완전히 제거하지 않아도 된다. DB 전환 중에는 파일 기반 서비스와 DB 기반 서비스를 비교할 수 있도록 작게 교체한다.

완료 조건:

- `/articles`가 DB Article 목록을 보여준다.
- `/articles/{slug}`가 DB Article 상세를 보여준다.
- 없는 slug는 404로 응답한다.
- 기존 Thymeleaf 템플릿 구조를 크게 바꾸지 않는다.

### 2단계: Category 이관

작업:

- `CategoryEntity` 작성
- Article과 Category 관계 연결
- 기존 category/subcategory 문자열을 계층 구조로 변환
- `articleService.findTopics()`를 DB 기반으로 변경

완료 조건:

- 아티클 목록의 카테고리/서브카테고리 필터 UI가 DB 데이터를 사용한다.
- 아티클 상세의 좌측 토픽 목록이 DB 데이터를 사용한다.
- 카테고리 표시 순서가 안정적으로 유지된다.

### 3단계: Tag 이관

작업:

- `TagEntity` 작성
- `ArticleTagEntity` 또는 명시적 관계 엔티티 작성
- Article 생성/수정 시 태그 연결 처리

완료 조건:

- Article에 여러 태그를 연결할 수 있다.
- 같은 태그가 중복 생성되지 않는다.
- 태그 삭제/변경 시 연결 데이터가 깨지지 않는다.

### 4단계: Article 작성/수정/삭제

작업:

- 작성 폼 DTO 작성
- 저장용 POST 라우트 추가
- 수정 폼과 수정 POST 라우트 추가
- 삭제 또는 archive 처리 추가
- 이미지 업로드가 필요하면 MinIO 업로드 후 object key 저장
- validation 적용

완료 조건:

- 새 글을 작성하면 DB에 저장된다.
- 저장 후 `/articles/{slug}`로 redirect 된다.
- 제목, slug, 본문 필수값 검증이 동작한다.
- slug 중복 시 사용자에게 에러가 표시된다.
- 삭제는 실제 delete보다 `ARCHIVED` 상태 변경부터 시작한다.
- 이미지 업로드를 구현했다면 DB에는 바이너리가 아니라 URL/object key만 저장된다.

### 5단계: Project 이관

작업:

- `ProjectEntity` 작성
- `ProjectRepository` 작성
- `ProjectService.findAll()`, `findBySlug()`를 DB 기반으로 변경
- 상세 HTML을 DB 컬럼으로 이관

완료 조건:

- `/project`가 DB Project 목록을 보여준다.
- `/project/{slug}`가 DB Project 상세를 보여준다.
- 기존 이미지/영상 경로가 깨지지 않는다.

### 6단계: Snippet 이관

작업:

- `SnippetEntity` 작성
- `SnippetRepository` 작성
- `SiteController.snippetsData()` 하드코딩 제거 또는 Service로 이동

완료 조건:

- `/snippets`가 DB Snippet 목록을 보여준다.
- language/tag 필드가 화면에 정상 표시된다.

### 7단계: About 데이터 이관 검토

About의 timeline, certification, skill은 자주 바뀌는 데이터가 아니므로 DB 이관이 필수는 아니다.

선택 기준:

- 관리자 화면에서 수정하고 싶으면 DB로 이관한다.
- 거의 바뀌지 않으면 파일/코드 유지도 가능하다.

## 작업 순서 체크리스트

- [ ] PostgreSQL 실행 방법 정리
- [ ] MinIO 실행 방법 정리
- [ ] Flyway migration 설정
- [ ] 첫 migration 작성
- [ ] `ArticleEntity` 작성
- [ ] `ArticleRepository` 작성
- [ ] Article seed 데이터 작성
- [ ] Article 목록 조회 DB 전환
- [ ] Article 상세 조회 DB 전환
- [ ] 없는 slug 404 확인
- [ ] Category 엔티티 추가
- [ ] Topic/sidebar DB 전환
- [ ] Article 작성 폼 저장 구현
- [ ] Article 수정 구현
- [ ] Article archive/delete 구현
- [ ] Project DB 전환
- [ ] Snippet DB 전환
- [ ] 테스트 체크리스트 수행

## 리스크와 대응

| 리스크 | 대응 |
| --- | --- |
| Entity를 화면에서 직접 너무 많이 사용 | 조회용 DTO 또는 record를 두고 템플릿이 필요한 필드만 전달 |
| Markdown HTML 변환 위치가 애매함 | 처음에는 Service에서 변환하고, 필요해지면 별도 renderer로 분리 |
| slug 중복으로 상세 페이지 충돌 | DB unique 제약과 validation을 함께 사용 |
| 이미지 경로가 깨짐 | DB에는 public URL 또는 object key만 저장하고 MinIO/S3 URL 생성 규칙을 분리 |
| Flyway migration이 반복 실패 | 이미 적용된 migration은 수정하지 않고 새 migration을 추가 |
| 로컬 MinIO와 실제 S3 차이 | S3-compatible API만 사용하고 provider 종속 옵션은 나중에 분리 |
| DB 이관 중 화면이 깨짐 | route와 template model key를 유지하며 Service 내부만 교체 |

## 완료 기준

1차 DB 이관 완료 기준:

- Article 목록/상세가 DB에서 조회된다.
- Article 작성/수정이 DB에 반영된다.
- Project 목록/상세가 DB에서 조회된다.
- `npm run verify`가 성공한다.
- [테스트 체크리스트](04-testing-checklist.md)의 핵심 항목이 통과한다.
