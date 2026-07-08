---
type: Architecture Decision
title: DB 기반 콘텐츠 전환 결정
description: DevArchive의 파일 기반 콘텐츠를 PostgreSQL, Flyway, MinIO 기반 DB/스토리지 구조로 이관하기로 한 결정 기록.
tags: ["decision", "backend", "database", "storage"]
timestamp: "2026-07-09T00:00:00+09:00"
---

# DB 기반 콘텐츠 전환 결정

## Context

DevArchive는 Spring Boot와 Thymeleaf SSR 셸로 전환됐지만, 콘텐츠 데이터는 아직 파일 기반이다.

- Article은 Markdown 파일에서 읽는다.
- Project는 하드코딩 metadata와 HTML 파일에서 읽는다.
- Snippet과 About 일부 데이터는 Controller 내부 하드코딩이다.

백엔드 구현 연습을 위해 이 데이터를 DB 기반 조회와 작성/수정 흐름으로 점진적으로 전환한다.

## Decision

다음 기준으로 진행한다.

- 메인 DB는 PostgreSQL을 사용한다.
- DB schema 변경 이력은 Flyway로 관리한다.
- Article/Project 본문 원본은 Markdown으로 저장한다.
- HTML은 렌더링 캐시가 필요해질 때 nullable `content_html` 컬럼으로 사용한다.
- 이미지와 영상 바이너리는 DB에 저장하지 않는다.
- DB에는 public URL 또는 object storage key만 저장한다.
- 로컬 object storage는 MinIO Docker 컨테이너를 사용한다.
- 실제 배포에서는 AWS S3, Cloudflare R2, Naver Object Storage 등 S3 호환 저장소로 교체 가능하게 둔다.
- 삭제는 실제 delete보다 `DRAFT`, `PUBLISHED`, `ARCHIVED` 상태값 기반으로 먼저 구현한다.

## Rationale

PostgreSQL은 Spring/JPA 학습에서 관계형 모델, 인덱스, JSON, text 타입, transaction을 폭넓게 연습하기 좋다. MySQL도 국내 Spring 채용에서 매우 유효하지만, 이 프로젝트에서는 PostgreSQL을 메인으로 잡고 MySQL과의 차이는 면접 대비 노트로 보완한다.

Flyway는 schema 변경 이력을 코드처럼 남길 수 있다. `schema.sql`만 사용하는 방식보다 실무적인 migration 흐름을 설명하기 좋고, 이미 적용된 migration을 수정하지 않고 새 migration으로 변경을 누적하는 습관을 만들 수 있다.

본문은 Markdown 원본을 보존한다. HTML만 저장하면 수정 화면과 렌더링 정책 변경에 취약하다. Markdown 원본을 두면 코드 하이라이트, 목차 생성, sanitize 정책을 바꿔도 다시 HTML을 생성할 수 있다.

이미지/영상은 object storage에 둔다. DB가 바이너리 파일 크기에 끌려가지 않고, 백업/복구/migration을 메타데이터 중심으로 유지할 수 있다. 파일 제공은 object storage와 CDN이 더 적합하며, 애플리케이션은 업로드와 URL/object key 관리에 집중한다.

MinIO는 로컬에서 S3 호환 API를 연습하기에 단순하다. AWS 계정 없이도 bucket, object key, upload/download 흐름을 구현할 수 있고, 나중에 실제 S3 호환 저장소로 옮길 때 구조를 크게 바꾸지 않아도 된다.

## Consequences

좋은 점:

- DB 이관 학습 범위가 명확해진다.
- schema 변경 이력이 Flyway migration으로 남는다.
- 콘텐츠 본문 원본과 렌더링 결과의 책임이 분리된다.
- 이미지/영상 저장 책임이 DB에서 분리된다.
- 포트폴리오에서 PostgreSQL, Flyway, object storage 경험을 설명할 수 있다.

주의할 점:

- Docker로 PostgreSQL과 MinIO를 함께 실행해야 한다.
- MinIO와 실제 S3 호환 저장소의 세부 권한/URL 정책 차이를 이해해야 한다.
- `content_html` 캐시를 도입하면 원본 Markdown과 캐시 동기화 정책이 필요하다.
- 테스트에서 H2를 쓰면 PostgreSQL 전용 SQL과 타입 차이를 조심해야 한다.

## Follow-up

- PostgreSQL Docker 실행 문서 또는 compose 파일 추가
- MinIO bucket 생성 절차 정리
- Flyway `V1__...sql` 작성
- Article Entity/Repository 구현
- Markdown renderer 책임 분리 검토
- StorageService 인터페이스 설계
