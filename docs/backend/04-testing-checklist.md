---
type: Backend Testing Checklist
title: Backend Testing Checklist
description: DB 기반 SSR 전환 중 확인해야 할 기능별 테스트 체크리스트.
tags: ["backend", "testing", "checklist", "verification"]
timestamp: "2026-07-09T00:00:00+09:00"
---

# Backend Testing Checklist

## 목적

이 문서는 DB 기반 SSR 구현 중 기능이 실제로 동작하는지 확인하기 위한 체크리스트다. 자동 테스트를 모두 작성하기 전에도, 최소 수동 검증 기준으로 사용할 수 있다.

## 공통 검증

- [ ] `npm run docs:validate`가 성공한다.
- [ ] `npm run verify`가 성공한다.
- [ ] 애플리케이션이 DB 연결 오류 없이 실행된다.
- [ ] PostgreSQL 컨테이너가 실행 중이다.
- [ ] Flyway migration이 성공한다.
- [ ] MinIO 콘솔에 접속할 수 있다.
- [ ] 이미지 bucket이 생성되어 있다.
- [ ] `/` 홈이 200으로 응답한다.
- [ ] 라이트/다크 모드에서 주요 화면 텍스트 대비가 유지된다.
- [ ] 모바일 폭에서 nav, 카드, 본문이 겹치지 않는다.

## Article 목록

- [ ] `/articles`가 200으로 응답한다.
- [ ] DB에 저장된 게시글 수만큼 목록이 표시된다.
- [ ] 최신순 또는 의도한 정렬 순서로 표시된다.
- [ ] 제목, 설명, 날짜, 카테고리가 표시된다.
- [ ] featured 글이 있다면 기존 UI 의도에 맞게 표시된다.
- [ ] 글이 0개일 때 빈 상태가 깨지지 않는다.
- [ ] 비공개 또는 archived 글은 공개 목록에서 제외된다.

## Article 상세

- [ ] `/articles/{slug}`가 200으로 응답한다.
- [ ] DB의 title, description, body가 화면에 표시된다.
- [ ] Markdown 또는 HTML 본문 렌더링이 깨지지 않는다.
- [ ] 이미지 경로가 깨지지 않는다.
- [ ] DB에는 이미지 바이너리가 아니라 URL/object key만 저장된다.
- [ ] 목차가 필요한 경우 heading 기반으로 생성된다.
- [ ] 없는 slug 접근 시 404로 응답한다.
- [ ] 다른 글의 데이터가 섞이지 않는다.

## Article 작성

- [ ] `/write`가 작성 폼을 렌더링한다.
- [ ] title, slug, description, body를 입력하면 저장된다.
- [ ] 저장 후 `/articles/{slug}`로 redirect 된다.
- [ ] 새로고침해도 중복 저장되지 않는다.
- [ ] 필수값 누락 시 validation 에러가 표시된다.
- [ ] slug 중복 시 사용자에게 에러가 표시된다.
- [ ] 잘못된 slug 형식이 차단된다.
- [ ] 이미지 업로드를 구현했다면 MinIO에 object가 생성된다.
- [ ] 이미지 업로드 실패 시 Article 저장 정책이 명확하다.

## Article 수정

- [ ] 기존 글 수정 폼이 현재 값을 채운 상태로 열린다.
- [ ] title, description, body 수정이 DB에 반영된다.
- [ ] slug 변경 정책이 명확하게 동작한다.
- [ ] 수정 후 상세 페이지로 redirect 된다.
- [ ] 없는 글 수정 접근 시 404로 응답한다.
- [ ] validation 실패 시 입력값이 유지된다.

## Article 삭제 또는 Archive

- [ ] 삭제 버튼 또는 archive 동작이 의도한 라우트로 요청된다.
- [ ] archived 글은 공개 목록에서 제외된다.
- [ ] archived 글 상세 접근 정책이 명확하다.
- [ ] 실제 delete를 사용한다면 관련 tag mapping이 정리된다.
- [ ] 삭제 후 목록으로 redirect 된다.

## Category와 Topic

- [ ] 최상위 카테고리가 표시된다.
- [ ] 서브카테고리가 부모 아래에 표시된다.
- [ ] 카테고리별 article count가 맞다.
- [ ] 현재 선택된 카테고리 active state가 맞다.
- [ ] 잘못된 category slug 요청 시 빈 목록 또는 404 정책이 일관된다.

## Tag

- [ ] Article에 여러 태그를 연결할 수 있다.
- [ ] 같은 태그가 중복 생성되지 않는다.
- [ ] 태그 제거 시 article 본문/상세가 깨지지 않는다.
- [ ] 태그 필터를 추가했다면 필터 결과가 맞다.

## Project

- [ ] `/project`가 DB Project 목록을 표시한다.
- [ ] `/project/{slug}`가 DB Project 상세를 표시한다.
- [ ] 이미지와 영상 경로가 깨지지 않는다.
- [ ] 프로젝트 태그가 표시된다.
- [ ] 없는 slug 접근 시 404로 응답한다.

## Snippet

- [ ] `/snippets`가 DB Snippet 목록을 표시한다.
- [ ] code, language, tag가 화면에 표시된다.
- [ ] 코드 줄바꿈이 유지된다.
- [ ] snippet이 0개일 때 화면이 깨지지 않는다.

## Repository 테스트 후보

자동 테스트를 추가한다면 우선순위는 다음과 같다.

- [ ] `findBySlug`가 존재하는 글을 찾는다.
- [ ] `findBySlug`가 없는 slug에 대해 empty를 반환한다.
- [ ] 공개 글만 최신순으로 조회된다.
- [ ] slug unique 제약이 동작한다.
- [ ] category 관계 조회가 동작한다.
- [ ] PostgreSQL 기준 migration schema와 Entity 매핑이 맞다.

## Service 테스트 후보

- [ ] Article 생성 시 slug 중복을 거부한다.
- [ ] Article 생성 시 기본 status가 적용된다.
- [ ] Article 상세 조회 실패 시 도메인 예외 또는 empty가 반환된다.
- [ ] Article 수정 시 허용된 필드만 변경된다.
- [ ] archive 처리 후 공개 목록에서 제외된다.
- [ ] Markdown 원본에서 HTML 변환 결과가 생성된다.
- [ ] 이미지 object key에서 public URL 생성이 가능하다.

## 완료 판정

1차 DB 전환은 다음 조건을 만족하면 완료로 본다.

- Article 목록/상세가 DB 기반으로 동작한다.
- Article 작성/수정/삭제 또는 archive 중 최소 작성과 수정이 동작한다.
- Project 목록/상세가 DB 기반으로 동작한다.
- `npm run verify`가 성공한다.
- 핵심 수동 검증 항목이 통과한다.
