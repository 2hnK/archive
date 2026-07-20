---
type: Design Reference
title: Color System
description: DevArchive의 CSS 변수, 테마 팔레트, 상태색 사용 규칙.
tags: ["design", "color", "tokens"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# Color System

## CSS Variables

`src/styles/global.css`의 현재 핵심 변수:

```css
:root {
  --bg-color: #f4f5f7;
  --text-color: #1a1a1a;
  --border-color: #1a1a1a;
  --accent-color: #1e66f5;
}

.dark {
  --bg-color: #0f0f0f;
  --text-color: #f4f0db;
  --border-color: #f4f0db;
  --accent-color: #89b4fa;
}
```

## Theme Palette

- Light background: `#f4f5f7`
- Light text/border: `#1a1a1a`
- Light accent: `#1e66f5`
- Dark background: `#0f0f0f`
- Dark text/border: `#f4f0db`
- Dark accent: `#89b4fa`

## Secondary State Colors

토픽, 목차, 뷰 토글, About 마일스톤과 공통 hover 상태에는 같은 블루 계열이 사용된다.

- Light active blue: `#1e66f5`
- Dark active blue: `#89b4fa`

블루는 공통 강조와 상태 표시를 잇는 단일 accent다. 넓은 면을 채우기보다 필터·타임라인·hairline·hover 텍스트처럼 목적이 분명한 곳에 제한한다. About 마일스톤은 `--milestone-accent-color`로 같은 라이트/다크 값을 전환한다.

스크롤 기반 번호처럼 현재 위치를 나타내는 묶음에서는 활성 항목 하나만 블루로 표시한다. 비활성 번호는 `--text-color`와 낮은 opacity를 유지한다.

기술 스택과 자격 로고는 식별성을 위한 예외다. Simple Icons와 공식 자격 로고는 원본 브랜드 색상을 상시 표시할 수 있으며, 이 색을 배경·버튼·페이지 accent로 확장하지 않는다.

## Usage Rules

- 새 색상 추가 전 기존 변수와 opacity 조합으로 해결한다.
- 라이트 배경은 색감이 강하지 않은 쿨그레이를 사용해 흰색 글래스 패널과의 명도 차이를 확보한다.
- 강조는 먼저 `--accent-color`를 사용한다.
- 보더는 `border-color`, `text-color`의 opacity, white/black opacity 계열을 우선한다.
- 페이지별 독립 팔레트를 만들지 않는다.
- `TimeProgress.astro`의 진행 막대 색상은 제한된 위젯 내부 상태색으로만 취급하고, 새 페이지의 브랜드 팔레트로 확장하지 않는다.
