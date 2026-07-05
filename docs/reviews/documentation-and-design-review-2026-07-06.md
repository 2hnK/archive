---
type: Review Report
title: 문서와 디자인 시스템 검토 기록
description: OKF와 하네스 적용 시점의 문서 품질, 디자인 일관성, 추가 검토사항 보고.
tags: ["review", "documentation", "design", "harness"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# 문서와 디자인 시스템 검토 기록

## 검토 범위

- `README.md`
- `AGENTS.md`
- `docs/**/*.md`
- `src/styles/global.css`
- `src/components/*.astro`
- 주요 페이지 패턴과 콘텐츠 컬렉션 구조

## 결론

현재 문서는 프로젝트의 Astro 정적 사이트 구조와 에디토리얼/글래스 디자인 방향을 대체로 정확히 설명하고 있다. README가 인덱스 역할을 하고, 상세 정책을 `docs/` 아래로 분리한 방향도 적절하다.

보강이 필요했던 영역은 문서의 기계적 검증, Git 작업 규칙, OKF frontmatter, 구현 파일과 디자인 문서의 대응 관계였다. 이번 정비에서 해당 항목을 문서와 하네스에 반영했다.

## 확인한 개선 사항

- 모든 추적 Markdown 문서에 OKF `type` frontmatter를 추가했다.
- `npm run docs:validate`로 OKF 필수 필드와 로컬 링크를 검증하도록 했다.
- `npm run verify`로 문서 검증, Astro 검사, 정적 빌드를 한 번에 실행하도록 했다.
- Git 브랜치, 커밋, 검증 규칙을 한국어 문서로 추가했다.
- 디자인 문서에 구현 기준 파일과 예외 규칙을 보강했다.

## 디자인 문서 검토

현재 디자인 문서는 다음 구현과 일치한다.

- `BaseLayout.astro`: 고정 내비게이션, 전역 폰트, 테마 스크립트, 공통 레이아웃
- `global.css`: 색상 변수, 글래스 유틸리티, prose, reveal, editorial list
- `Navbar.astro`: 글래스 내비게이션과 sliding highlight
- `ArticleCard.astro`: 이미지/placeholder 카드와 hover scale
- `TopicsSidebar.astro`: 카테고리 계층, active blue, sliding highlight

추가로 `TimeProgress.astro`는 생산성 위젯 성격이 강해 공개 아카이브의 기본 팔레트보다 다양한 진행 색상을 사용한다. 이 색상은 전역 브랜드 팔레트가 아니라 제한된 위젯 내부 상태색으로 취급해야 한다.

## 추가 검토사항

- `npm audit --omit=dev` 기준 취약점 15건이 보고되었다. 주요 항목은 Astro, Vite, esbuild, fast-uri, picomatch 계열 전이 의존성이다. 자동 수정은 잠금파일과 런타임 범위가 넓어 이번 작업에서는 적용하지 않았고, 별도 의존성 보안 점검 작업으로 분리하는 것이 맞다.
- `npm run verify`는 통과하지만 `astro check`가 unused/deprecated 힌트를 출력한다. 실패 조건은 아니지만, 장기적으로는 `public/liquid-glass.js`, `src/content.config.ts`, 일부 페이지의 미사용 변수 정리를 별도 유지관리 작업으로 분리할 수 있다.
- `Navbar.astro`의 GitHub/Instagram 링크는 각각 `https://github.com`, `https://instagram.com`으로 되어 있다. 소개 페이지의 GitHub 링크처럼 실제 프로필 URL로 교체할지 확인이 필요하다.
- UI 변경 빈도가 늘어나면 Playwright 기반 화면 검증과 스크린샷 비교를 하네스에 추가하는 것이 좋다.

## 검증 결과

- `npm run docs:validate`: 통과, 23개 Markdown 파일 확인
- `npm run verify`: 통과, 10개 정적 페이지 빌드
- `npm audit --omit=dev`: 실패, 취약점 15건 보고
