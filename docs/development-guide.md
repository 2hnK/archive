---
type: Development Guide
title: Development Guide
description: DevArchive 개발 요구사항, 명령, HTML/CSS 작성 기준, 검증 절차.
tags: ["development", "astro", "verification"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# Development Guide

## Requirements

- Node.js `>=18.14.0`
- npm

## Commands

```sh
npm install
npm run dev
npm run docs:validate
npm run check
npm run build
npm run verify
npm run preview
```

## Development Principles

- 현재 Astro 정적 사이트 구조를 유지한다.
- 새 페이지는 `BaseLayout.astro`를 우선 사용한다.
- 전역 디자인 규칙은 `src/styles/global.css`의 변수와 컴포넌트 클래스를 먼저 확인한다.
- 기존 클래스와 레이아웃 구조를 바꾸기보다 필요한 부분을 좁게 확장한다.
- 콘텐츠 추가는 가능한 한 Markdown content collection 흐름을 따른다.
- 문서 변경은 [OKF 문서 형식](knowledge-format.md)을 따르고 `npm run docs:validate`로 확인한다.
- 커밋 전 검증과 커밋 메시지는 [Git 컨벤션과 작업 규칙](git-conventions.md)을 따른다.

## HTML And CSS Guidelines

- HTML 구조는 페이지별 역할이 분명하도록 유지한다.
- 공통 UI는 컴포넌트로 분리하되, 단순 반복이 아닌 경우 과도하게 추상화하지 않는다.
- 기존 Tailwind 유틸리티 조합을 먼저 재사용한다.
- `glass-panel`, `glass-pill`, `custom-glass-highlight`, `editorial-list`, `reveal-up`, `prose`와 같은 기존 공통 스타일을 우선한다.
- 반응형 기준은 기존 `sm`, `md`, `lg`, `xl` 분기와 폭 제한을 따른다.

## Adding Articles

1. `src/content/articles/`에 Markdown 파일을 추가한다.
2. 기존 아티클의 frontmatter 구조를 따른다.
3. 이미지가 필요하면 아티클 이미지 폴더를 함께 둔다.
4. 목록, 상세, 필터에서 노출이 깨지지 않는지 확인한다.

## Adding Pages

1. `src/pages/`에 Astro 파일을 추가한다.
2. `BaseLayout.astro`를 사용한다.
3. 상단 고정 내비게이션을 고려해 충분한 top padding을 둔다.
4. `docs/design/page-patterns.md`의 기존 페이지 패턴 중 가장 가까운 구조를 따른다.
5. `npm run build`로 정적 빌드를 확인한다.

## Verification

변경 후 최소한 다음을 확인한다.

- `npm run verify`
- 라이트/다크 모드에서 주요 화면 확인
- 데스크톱/모바일 폭에서 내비게이션, 카드, 본문 폭 확인
- 새 CSS가 기존 규칙과 중복되거나 충돌하지 않는지 확인
