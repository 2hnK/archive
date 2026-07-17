---
type: Component Reference
title: Components
description: DevArchive 공통 컴포넌트와 재사용 가능한 CSS 패턴 기준.
tags: ["design", "components", "css"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# Components

## Navbar

`src/components/Navbar.astro`

- 화면 상단 고정
- 반투명 배경과 강한 blur
- 중앙 nav link는 대문자, 작은 글자, sliding highlight 사용
- 우측 아이콘 버튼은 원형 hover와 색상 변화 사용
- 모바일에서도 GitHub, Instagram, 테마, 메뉴 액션을 유지하되 32px 크기로 밀도를 조절
- 모바일 메뉴는 글래스 톤을 유지하되 배경 위에서도 링크가 선명한 전용 고투명도 드롭다운 사용

## Footer

`src/components/Footer.astro`

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

`src/components/ArticleCard.astro`

- 피드 카드와 같은 `glass-panel` 컨테이너와 큰 곡률 사용
- 내부 이미지는 한 단계 작은 곡률로 분리하고, 이미지 또는 카테고리 기반 placeholder 표시
- 카테고리, 날짜, 제목, 설명 순서
- 하단 hairline 위에 subcategory와 `Read Article` 링크 배치
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

`src/components/TopicsSidebar.astro`

- 카테고리/서브카테고리 계층 목록
- active state는 `#1e66f5`, dark mode는 `#89b4fa`
- `custom-glass-highlight`로 현재 항목과 hover 항목을 표시
- `reveal-up`과 `stagger-1`을 사용해 본문과 같은 진입 리듬 유지

## Time Progress

`src/components/TimeProgress.astro`

- 시간 진행률을 표시하는 도구형 위젯
- `bg-white/50`, `dark:bg-white/5`, blur, border, shadow를 사용해 글래스 톤과 연결
- 진행 막대에는 year/month/day/hour/minute별 상태색을 사용
- 이 색상은 전역 브랜드 팔레트가 아니라 위젯 내부 상태 표현으로만 사용

## Pagination

`.pagination-button`, `.pagination-ellipsis`

- 아티클 목록 하단의 이전, 페이지 번호, 다음 이동에 사용
- 원형 글래스 버튼과 텍스트/배경 반전 active 상태를 사용
- 필터 결과에 따라 페이지 수를 다시 계산하고 URL의 `page` 쿼리를 갱신
- 페이지가 많으면 현재 페이지 주변과 처음/마지막 페이지 사이를 ellipsis로 축약
