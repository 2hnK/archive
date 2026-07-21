---
type: Component Reference
title: Components
description: DevArchive 공통 컴포넌트와 재사용 가능한 CSS 패턴 기준.
tags: ["design", "components", "css"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# Components

## Navbar

`src/components/Navbar.astro`

- 화면 상단 고정
- 반투명 배경과 강한 blur
- 홈에서는 야간 히어로와 이어지는 어두운 저투명도 glass 변형을 사용하고 링크·아이콘을 따뜻한 흰색으로 표시하며, 히어로를 벗어나면 현재 라이트·다크 테마의 기본 표면과 텍스트 색으로 복귀
- 중앙 nav link는 대문자, 작은 글자, sliding highlight 사용
- 우측 아이콘 버튼은 원형 hover와 색상 변화 사용
- 모바일에서도 GitHub, Instagram, 테마, 메뉴 액션을 유지하되 32px 크기로 밀도를 조절
- 모바일 메뉴는 글래스 톤을 유지하되 배경 위에서도 링크가 선명한 전용 고투명도 드롭다운 사용

## Footer

`src/components/Footer.astro`

- 화면 좌우에 맞닿는 얇은 `glass-panel` 밴드를 사용해 푸터 영역임을 명확히 한다.
- 브랜드, Navigation, Contact는 데스크톱에서 한 행에 배치하고 모바일에서만 세로로 쌓는다.
- 브랜드 위에는 파란 짧은 선과 `Archive footer / 연도` 메타 라벨을 두어 About의 에디토리얼 문법을 잇는다.
- 하단 hairline에는 저작권·지역과 `Back to top`을 배치한다.
- 큰 곡률과 넓은 내부 여백은 피하고, 링크의 짧은 underline 확장과 화살표의 2px 상승만 사용한다.

## Glass Panel

`.glass-panel`

- 반투명 배경
- `backdrop-filter: blur(...) saturate(...)`
- 얇은 반투명 border
- 외부 shadow와 내부 highlight
- 카드, 이미지 래퍼, 모바일 메뉴, 타임라인 노드에 사용
- 반복 데이터를 묶는 register/directory 표면에도 사용하며 내부 항목은 hairline으로 나눈다.

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

- 피드 카드와 같은 `glass-panel` 컨테이너와 큰 곡률을 사용한다.
- 내부 이미지는 한 단계 작은 곡률로 분리하고, 이미지 또는 카테고리 기반 placeholder를 표시한다.
- 카테고리, 날짜, 제목, 설명 순서로 구성한다.
- 하단 hairline 위에 subcategory와 `Read Article` 링크를 배치한다.
- 제목 hover 시 accent color, 이미지 hover 시 미세한 scale을 적용한다.

## Home Content Cards

`src/components/HomeArticleCard.astro`, `src/components/HomeProjectCard.astro`

- 홈 아티클 카드는 모바일에서 이미지와 본문을 쌓고, 넓은 화면에서는 썸네일과 메타·제목·설명을 좌우로 배치하는 compact glass card다.
- 홈 프로젝트 카드는 기존 프로젝트 대표 이미지를 전체 배경으로 사용하고 하단 gradient 위에 연도, 제목, 설명, 기술 태그를 배치한다.
- 두 카드 모두 홈의 요약 탐색에만 사용하며 공용 `ArticleCard`와 프로젝트 인덱스 카드의 구조를 대체하지 않는다.
- hover는 accent border·텍스트, 이미지 약 2.5% 확대, 화살표 1px 이동 범위로 제한하고 `prefers-reduced-motion`에서는 transform transition을 제거한다.

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

- 초기 opacity 0, translateY 24px
- active 상태에서 opacity 1, translateY 0
- `stagger-1`, `stagger-2`, `stagger-3`는 100ms 안팎의 짧은 간격으로 순차 진입
- 전역 reveal과 React island를 같은 요소에 중복 적용하지 않는다.

## React Bits Interaction Islands

`src/components/react-bits/`

- React Bits의 시각 효과는 페이지 전체를 대체하지 않고, 기존 Astro 마크업 안의 작은 React island로만 사용한다.
- `BlurText`는 About 인사말을 단어 단위로 한 번만 드러내며, 제목의 크기와 줄바꿈은 Astro 마크업과 전역 타이포그래피가 결정한다.
- `AnimatedContent`는 About 정보 섹션의 첫 진입만 보조한다. 섹션 내부 hover와 링크는 정적 HTML/CSS로 유지한다.
- Home은 배경 사진, 타이포그래피, `reveal-up`, `editorial-list`만 사용하며 React island를 두지 않는다.
- 프로필 사진은 React 효과와 장식 오버레이를 사용하지 않는다. 이미지는 3:4 비율과 고정 크기를 유지하고, 흰색 계열 테두리와 절제된 그림자의 카드만 마우스 위치에 따라 최대 약 2도 틸트한다.
- `prefers-reduced-motion`에서는 BlurText와 AnimatedContent 이동, 프로필 틸트를 멈추고 정적인 최종 형태를 제공한다.
- 새 React Bits 효과는 기존 두 island로 해결할 수 없는 이유와 결정 문서 갱신 없이 추가하지 않는다.

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
