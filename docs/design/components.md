# Components

## Navbar

`src/components/Navbar.astro`

- 화면 상단 고정
- 반투명 배경과 강한 blur
- 중앙 nav link는 대문자, 작은 글자, sliding highlight 사용
- 우측 아이콘 버튼은 원형 hover와 색상 변화 사용
- 모바일 메뉴는 `glass-panel` 기반 드롭다운

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
