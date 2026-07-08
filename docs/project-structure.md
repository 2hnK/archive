---
type: Project Structure
title: Project Structure
description: DevArchive 저장소의 주요 디렉터리와 Spring SSR 소스 구조.
tags: ["structure", "spring", "thymeleaf", "docs"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# Project Structure

## Root

- `README.md`: 프로젝트 문서 인덱스
- `AGENTS.md`: AI 에이전트 작업 규칙
- `docs/`: 상세 문서
- `docs/backend/`: DB 이관, Spring SSR 구현, 테스트, 트러블슈팅 학습 문서
- `docs/decisions/`: 중요한 설계 결정 기록
- `docs/reviews/`: 문서, 디자인, 품질 검토 기록
- `scripts/`: 로컬 검증과 유지관리 스크립트
- `build.gradle`, `settings.gradle`, `gradlew.bat`: Spring Boot/Gradle 빌드 구성
- `package.json`: Tailwind CSS와 문서 검증 스크립트
- `src/main/java/`: Spring Boot 애플리케이션, 컨트롤러, 콘텐츠 서비스
- `src/main/resources/templates/`: Thymeleaf 페이지와 fragment
- `src/main/resources/static/`: favicon, 이미지, 영상, 클라이언트 스크립트
- `src/main/resources/content/`: 파일 기반 아티클/프로젝트 콘텐츠
- `src/main/resources/styles/global.css`: Tailwind 입력 CSS와 디자인 토큰
- `build/`: Gradle 빌드 결과물

`node_modules/`, `build/`, `.gradle/`, `.dump/`는 문서 하네스와 커밋 대상에서 제외한다.

## Source Tree

- `src/main/java/com/devarchive/web/`: 화면 컨트롤러와 공통 모델
- `src/main/java/com/devarchive/article/`: Markdown 아티클 로딩, frontmatter 파싱, 목차 생성
- `src/main/java/com/devarchive/project/`: 프로젝트 데이터와 상세 HTML 로딩
- `src/main/resources/templates/fragments/`: 내비게이션, 푸터, 카드, 토픽 사이드바 fragment
- `src/main/resources/templates/articles/`: 아티클 목록과 상세 템플릿
- `src/main/resources/templates/project/`: 프로젝트 목록과 상세 템플릿
- `src/main/resources/content/articles/`: Markdown 아티클 콘텐츠
- `src/main/resources/content/projects/`: 프로젝트 상세 HTML 콘텐츠

## Layouts

`src/main/resources/templates/layout/base.html`이 현재 사이트의 기본 레이아웃이다. Google Fonts, Material Symbols, 전역 CSS, 테마 적용 스크립트, `navbar`, `footer` fragment를 포함한다.

## Pages

- `/`: 큰 에디토리얼 히어로와 Articles/Works 목록
- `/articles`: 아티클 피드/그리드 목록, 카테고리 필터, 토픽 사이드바
- `/articles/[slug]`: 아티클 상세, 본문 카드, 좌측 토픽, 우측 목차
- `/project`: 프로젝트 카드 목록
- `/project/[slug]`: 프로젝트 상세 기록
- `/about`: 소개, 이력, 기술 스택, 자격 정보
- `/write`, `/write-project`, `/snippets`: 작성/보조/실험 성격의 정적 도구 페이지

## Content

아티클은 `src/main/resources/content/articles/` 아래 Markdown 파일로 관리한다. 이미지는 `src/main/resources/static/content/articles/images/`에도 정적 리소스로 제공한다.

아티클 Markdown도 OKF `type` frontmatter를 갖고, 렌더링에 필요한 필드는 `ArticleService`의 파일 기반 파서가 읽는다.

## Scripts

- `scripts/validate-docs.mjs`: Git이 추적하는 Markdown의 OKF frontmatter와 로컬 링크를 검증한다.
- `npm run docs:validate`: 문서 검증만 실행한다.
- `npm run verify`: 문서 검증, CSS 빌드, Gradle 테스트/빌드를 순서대로 실행한다.

## Backend Learning Docs

- `docs/backend/01-erd.md`: 파일 기반 콘텐츠를 DB 테이블로 옮기기 위한 ERD 초안
- `docs/backend/02-migration-plan.md`: 단계별 DB 이관 계획과 완료 기준
- `docs/backend/03-implementation-guide.md`: Spring MVC, JPA, Thymeleaf 구현 기준
- `docs/backend/04-testing-checklist.md`: 기능별 수동/자동 테스트 후보
- `docs/backend/05-troubleshooting.md`: 구현 중 반복되는 에러의 확인 순서와 해결 기록
