---
type: Component Reference
title: Components
description: DevArchive 공통 컴포넌트와 재사용 가능한 CSS 패턴 기준.
tags: ["design", "components", "css"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# Components

## Navbar

`src/main/resources/templates/fragments/navbar.html`

- 화면 상단 고정
- 반투명 배경과 강한 blur
- 중앙 nav link는 대문자, 작은 글자, sliding highlight 사용
- 우측 아이콘 버튼은 원형 hover와 색상 변화 사용
- 모바일 메뉴는 `glass-panel` 기반 드롭다운

## Footer

`src/main/resources/templates/fragments/footer.html`

- 상단 border
- 중앙 정렬
- 작은 대문자 저채도 텍스트

## Glass Panel

`.glass-panel`

- 반투명 배경
- `backdrop-filter: blur(...) saturate(...)`
- 얇은 반투명 border
- 외부 shadow와 내부 highlight
- 카드, 이미지 래퍼, 모바일 메뉴, 타임라인 노드에 사용

## Glass Pill

`.glass-pill`

- `rounded-full`
- 반투명 배경과 blur
- 태그, 토글, 연도 badge, chip에 사용

## Custom Glass Highlight

`.custom-glass-highlight`

- sliding highlight, active indicator, hover 배경에 사용
- nav, category, toc, toggle 같은 상태성 UI에 적합

## Article Card

`src/main/resources/templates/fragments/article-card.html`

- 이미지 또는 카테고리 기반 placeholder
- 카테고리, 날짜, 제목, 설명 순서
- 제목 hover 시 accent color
- 이미지 hover scale

## Editorial List

`.editorial-list`, `.editorial-list-item`

- 1px border 기반 목록
- hover 시 배경/텍스트 반전
- hover 시 좌우 padding 증가
- arrow icon 회전

## Prose

`.prose`

- Markdown 본문 렌더링 기준
- 산세리프 본문, 세리프 heading
- 넉넉한 line-height
- 코드, 링크, blockquote 스타일 포함

## Reveal Motion

`.reveal-up`

- 초기 opacity 0, translateY 60px
- active 상태에서 opacity 1, translateY 0
- `stagger-1`, `stagger-2`, `stagger-3`로 순차 진입

## Topics Sidebar

`src/main/resources/templates/fragments/topics-sidebar.html`

- 카테고리/서브카테고리 계층 목록
- active state는 `#1e66f5`, dark mode는 `#89b4fa`
- `custom-glass-highlight`로 현재 항목과 hover 항목을 표시
- `reveal-up`과 `stagger-1`을 사용해 본문과 같은 진입 리듬 유지

## Tool Buttons

`.btn-premium`

- 작성 보조 페이지의 복사/다운로드 버튼에 사용
- 기존 zinc 계열 form UI와 충돌하지 않도록 얇은 border, 작은 산세리프 라벨, accent hover를 사용
- 공개 아카이브 페이지의 주요 CTA가 아니라 도구형 보조 명령으로만 사용
