---
type: Design Reference
title: Color System
description: DevArchive의 CSS 변수, 테마 팔레트, 상태색 사용 규칙.
tags: ["design", "color", "tokens"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# Color System

## CSS Variables

`src/styles/global.css`의 현재 핵심 변수:

```css
:root {
  --bg-color: #ffffff;
  --text-color: #1a1a1a;
  --border-color: #1a1a1a;
  --accent-color: #D32F2F;
}

.dark {
  --bg-color: #0f0f0f;
  --text-color: #f4f0db;
  --border-color: #f4f0db;
  --accent-color: #ff4d4d;
}
```

## Theme Palette

- Light background: `#ffffff`
- Light text/border: `#1a1a1a`
- Light accent: `#D32F2F`
- Dark background: `#0f0f0f`
- Dark text/border: `#f4f0db`
- Dark accent: `#ff4d4d`

## Secondary State Colors

토픽, 목차, 뷰 토글의 활성 상태에는 기존 블루 계열이 사용된다.

- Light active blue: `#1e66f5`
- Dark active blue: `#89b4fa`

이 색은 이미 구현된 상태 표시용 보조색으로 참고한다. 새 브랜드 컬러처럼 넓게 쓰기보다, 필터나 active state처럼 목적이 분명한 곳에 맞춰 사용한다.

## Usage Rules

- 새 색상 추가 전 기존 변수와 opacity 조합으로 해결한다.
- 강조는 먼저 `--accent-color`를 사용한다.
- 보더는 `border-color`, `text-color`의 opacity, white/black opacity 계열을 우선한다.
- 페이지별 독립 팔레트를 만들지 않는다.
- `TimeProgress.astro`의 진행 막대 색상은 제한된 위젯 내부 상태색으로만 취급하고, 새 페이지의 브랜드 팔레트로 확장하지 않는다.
