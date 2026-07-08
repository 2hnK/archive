---
type: Backend Troubleshooting Guide
title: Backend Troubleshooting
description: Spring Boot, JPA, Thymeleaf 구현 중 자주 만나는 문제와 확인 순서.
tags: ["backend", "troubleshooting", "spring", "jpa"]
timestamp: "2026-07-09T00:00:00+09:00"
---

# Backend Troubleshooting

## 목적

이 문서는 구현 중 막혔을 때 증상, 원인 후보, 확인 순서, 해결 예시를 기록하는 문서다.

구현 가이드가 "어떻게 만들지"를 다룬다면, 트러블슈팅은 "왜 안 되는지"를 좁혀가는 문서다. 직접 만난 에러는 이 문서에 계속 추가한다.

## 기록 형식

새 문제를 만나면 아래 형식으로 추가한다.

```md
## 문제 이름

### 증상

화면 또는 로그에 나타난 현상.

### 원인 후보

- 가능한 원인 1
- 가능한 원인 2

### 확인 순서

1. 먼저 확인할 것
2. 다음으로 확인할 것

### 해결

실제로 해결한 방법.
```

## Template Not Found

### 증상

라우트에 접근했을 때 Thymeleaf가 template을 찾지 못한다.

대표 로그:

```text
TemplateInputException: Error resolving template
```

### 원인 후보

- Controller의 return 값과 template 경로가 다르다.
- `src/main/resources/templates/` 아래에 파일이 없다.
- 파일명 또는 폴더명이 다르다.
- redirect가 필요한 곳에서 template 이름을 반환했다.

### 확인 순서

1. Controller의 `return "..."` 값을 확인한다.
2. `src/main/resources/templates/` 아래 실제 경로를 확인한다.
3. 확장자 `.html`이 있는지 확인한다.
4. Gradle build 결과에 resources가 포함되는지 확인한다.

### 해결 예시

```java
return "articles/detail";
```

위 값은 다음 파일을 찾는다.

```text
src/main/resources/templates/articles/detail.html
```

## Whitelabel Error Page

### 증상

브라우저에 Whitelabel Error Page가 표시된다.

### 원인 후보

- Controller 내부 예외
- template 렌더링 중 model attribute 누락
- DB 조회 실패
- 없는 slug에 대한 처리 누락

### 확인 순서

1. 터미널 로그의 첫 번째 `Caused by`를 확인한다.
2. 요청 URL과 Controller 메서드가 맞는지 확인한다.
3. template에서 참조하는 model 이름이 Controller에서 추가됐는지 확인한다.
4. DB 조회 결과가 비어 있을 때 처리했는지 확인한다.

### 해결

없는 데이터는 500이 아니라 404로 처리한다.

```java
articleService.findBySlug(slug)
    .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND));
```

## Repository Bean 생성 실패

### 증상

애플리케이션 시작 시 Repository 관련 bean 생성에 실패한다.

대표 로그:

```text
No qualifying bean of type
Not a managed type
```

### 원인 후보

- Entity에 `@Entity`가 없다.
- Entity package가 Spring Boot component scan 범위 밖이다.
- Repository generic 타입이 잘못됐다.
- `JpaRepository<ArticleEntity, Long>`의 id 타입이 Entity와 다르다.

### 확인 순서

1. Entity 클래스에 `@Entity`가 있는지 확인한다.
2. Entity가 `com.devarchive` 하위 package에 있는지 확인한다.
3. Repository가 `JpaRepository<Entity, IdType>` 형태인지 확인한다.
4. Entity의 `@Id` 타입과 Repository id 타입이 같은지 확인한다.

## DB 연결 실패

### 증상

애플리케이션 시작 시 datasource 또는 connection 오류가 발생한다.

### 원인 후보

- DB 서버가 실행되지 않았다.
- JDBC URL이 틀렸다.
- username/password가 틀렸다.
- driver dependency가 없다.
- profile이 의도와 다르게 적용됐다.

### 확인 순서

1. DB가 실행 중인지 확인한다.
2. `application.properties`의 `spring.datasource.url`을 확인한다.
3. 계정과 비밀번호를 확인한다.
4. `build.gradle`에 DB driver dependency가 있는지 확인한다.
5. active profile을 확인한다.

## Flyway Migration 실패

### 증상

애플리케이션 시작 시 Flyway migration 오류가 발생한다.

대표 로그:

```text
FlywayException
Validate failed
Migration checksum mismatch
```

### 원인 후보

- 이미 적용된 migration 파일을 수정했다.
- SQL 문법이 PostgreSQL과 맞지 않는다.
- 테이블 또는 컬럼이 이미 존재한다.
- migration 파일명이 `V1__description.sql` 형식을 따르지 않는다.

### 확인 순서

1. 오류가 난 migration version을 확인한다.
2. `flyway_schema_history` 테이블을 확인한다.
3. 이미 적용된 migration 파일을 수정했는지 확인한다.
4. PostgreSQL에서 SQL을 직접 실행해 문법 오류를 확인한다.

### 해결 원칙

이미 공유되거나 적용된 migration은 수정하지 않고 새 migration을 추가한다.

```text
V1__create_articles.sql
V2__add_article_status.sql
```

## Entity 매핑 실패

### 증상

애플리케이션 시작 또는 Repository 호출 시 테이블/컬럼 매핑 오류가 난다.

### 원인 후보

- DB 테이블 이름과 Entity `@Table` 이름이 다르다.
- 컬럼 이름이 다르다.
- `nullable = false`인데 seed 데이터에 null이 있다.
- enum 저장 방식이 맞지 않는다.

### 확인 순서

1. Entity의 `@Table(name = "...")` 확인
2. 각 필드의 `@Column(name = "...")` 확인
3. 실제 DB schema 확인
4. seed 데이터의 필수값 누락 여부 확인

## MinIO 연결 실패

### 증상

이미지 업로드 또는 조회 시 object storage 연결 오류가 발생한다.

### 원인 후보

- MinIO 컨테이너가 실행되지 않았다.
- endpoint, access key, secret key가 다르다.
- bucket이 생성되지 않았다.
- 애플리케이션에서 path-style access 설정이 필요하다.

### 확인 순서

1. `http://localhost:9001` 콘솔에 접속한다.
2. bucket이 존재하는지 확인한다.
3. 애플리케이션 설정의 endpoint와 credentials를 확인한다.
4. SDK client가 `http://localhost:9000` API endpoint를 바라보는지 확인한다.

## 이미지 URL은 저장됐지만 화면에 표시되지 않음

### 증상

DB에는 `image_url` 또는 `image_object_key`가 저장되어 있지만 브라우저에서 이미지가 보이지 않는다.

### 원인 후보

- DB에 저장된 값이 object key인지 public URL인지 섞였다.
- bucket 또는 object가 public read가 아니다.
- 애플리케이션이 object key를 URL로 변환하지 않았다.
- HTML 본문 이미지 경로 rewrite가 누락됐다.

### 확인 순서

1. DB 컬럼 값이 URL인지 object key인지 확인한다.
2. 브라우저 network tab에서 이미지 요청 URL과 응답 코드를 확인한다.
3. MinIO 콘솔에서 object가 실제로 존재하는지 확인한다.
4. public URL 방식인지 presigned URL 방식인지 정책을 확인한다.

## Form 값이 DTO에 바인딩되지 않음

### 증상

POST 요청은 들어오지만 DTO 필드가 null 또는 빈 값이다.

### 원인 후보

- input의 `name`이 DTO 필드명과 다르다.
- Thymeleaf에서 `th:field`가 잘못됐다.
- `@ModelAttribute` 이름이 template의 `th:object`와 다르다.
- setter가 없거나 record/class 선택이 바인딩 방식과 맞지 않는다.

### 확인 순서

1. form의 `th:object` 확인
2. input의 `th:field` 확인
3. Controller 파라미터의 `@ModelAttribute` 이름 확인
4. DTO에 기본 생성자와 setter가 필요한 구조인지 확인

### 해결 예시

```html
<form th:object="${articleForm}" method="post">
  <input th:field="*{title}" />
</form>
```

```java
public String create(@ModelAttribute("articleForm") ArticleForm form) {
    ...
}
```

## Validation 에러가 화면에 표시되지 않음

### 증상

validation은 실패하는데 화면에 에러 메시지가 보이지 않는다.

### 원인 후보

- `BindingResult` 위치가 잘못됐다.
- validation 실패 시 redirect하고 있다.
- template에서 `#fields.hasErrors()`를 사용하지 않는다.
- `th:object` 이름이 다르다.

### 확인 순서

1. `BindingResult`가 `@Valid` 파라미터 바로 뒤에 있는지 확인한다.
2. 에러 발생 시 `return "write"`처럼 template을 직접 반환하는지 확인한다.
3. template에 field error 출력 코드가 있는지 확인한다.

### 해결 원칙

validation 실패 시 redirect하지 않는다. redirect하면 `BindingResult`가 사라진다.

## LazyInitializationException

### 증상

template 렌더링 중 연관 객체를 읽을 때 지연 로딩 예외가 발생한다.

대표 로그:

```text
LazyInitializationException: could not initialize proxy
```

### 원인 후보

- Service 트랜잭션이 끝난 뒤 template에서 lazy 관계를 읽는다.
- Entity를 그대로 view에 넘기고 있다.
- 필요한 연관 데이터를 fetch하지 않았다.

### 확인 순서

1. template에서 어떤 연관 필드를 읽는지 확인한다.
2. Service 조회 메서드에 `@Transactional(readOnly = true)`가 있는지 확인한다.
3. Repository 조회에서 필요한 관계를 fetch join 또는 EntityGraph로 가져오는지 확인한다.
4. DTO로 변환해 template에 넘기는 구조를 검토한다.

### 권장 해결

조회 Service 안에서 필요한 데이터를 DTO로 변환해 반환한다.

## Slug 중복 오류

### 증상

글 저장 시 DB unique constraint 오류가 발생한다.

### 원인 후보

- 이미 존재하는 slug로 저장했다.
- validation 전에 저장을 시도했다.
- 수정 시 자기 자신의 slug도 중복으로 판단했다.

### 확인 순서

1. DB에 같은 slug가 있는지 확인한다.
2. Service에서 `existsBySlug`를 먼저 확인하는지 본다.
3. 수정 로직에서는 현재 article id를 제외하고 중복 검사하는지 확인한다.

### 해결 원칙

DB unique 제약은 마지막 안전장치로 두고, 사용자에게는 저장 전 validation 메시지를 보여준다.

## 없는 Slug 접근 시 500 발생

### 증상

존재하지 않는 `/articles/{slug}` 접근 시 404가 아니라 500이 발생한다.

### 원인 후보

- `Optional.get()`을 바로 호출했다.
- null을 template에 넘겼다.
- 예외 처리가 없다.

### 해결

```java
var article = articleService.findBySlug(slug)
    .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND));
```

## 계속 추가할 항목

- seed data 중복 insert
- Markdown 변환 결과 XSS 처리
- redirect 후 flash attribute 누락
- enum 값 변경 후 기존 데이터 오류
