---
type: Design Principles
title: Design Principles
description: DevArchive의 에디토리얼 글래스 아카이브 디자인 원칙.
tags: ["design", "principles", "editorial", "glass"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# Design Principles

## Extend From The Archive Tone

DevArchive는 제품 랜딩 페이지보다 개인 개발 아카이브에 가깝다. 화면은 설명을 과하게 늘어놓기보다 제목, 기록, 목록, 본문을 명확하게 보여준다.

새 요소를 만들 때는 이 톤을 고정된 규칙으로 묶기보다, 기존 화면에서 반복된 스타일을 출발점으로 삼아 자연스럽게 확장한다.

## Editorial First

큰 제목은 영문 `Newsreader`와 한글 `Noto Serif KR` 기반 세리프로 에디토리얼 인상을 만들고, 본문과 UI 조작 요소는 영문 `Manrope`와 한글 `Noto Sans KR` 기반 산세리프로 정리한다.

## High Contrast With Restrained Accent

기본 색은 흰색/검정 또는 다크 배경/크림 텍스트다. 강조는 레드 계열 `--accent-color`를 우선 사용한다. 아티클 필터처럼 상태 표시가 필요한 곳은 기존 블루 계열을 참고한다. 새 색상이 필요하면 기존 변수와 조화를 이루는지 먼저 확인한다.

## Glass As Container

주요 카드와 내비게이션은 반투명 배경, blur, 얇은 보더, 내부 하이라이트를 사용한다. 글래스 효과는 장식이 아니라 콘텐츠 그룹을 구분하는 컨테이너 역할이다.

## Motion Is Slow And Minimal

진입 애니메이션은 `reveal-up`처럼 opacity와 translate 중심의 흐름을 우선 참고한다. hover는 scale, color, opacity, arrow rotation 같은 기존 반응과 비슷한 밀도에서 확장한다.

## Static Structure First

이 프로젝트는 정적 HTML/CSS/Astro 기반 사이트다. 디자인 일관성을 위해 현재 구조를 기본값으로 삼고, 큰 구조 변경이나 UI 라이브러리 도입은 명확한 필요가 있을 때만 검토한다.

## Implementation Is The Source

디자인 문서는 구현을 설명하고 가이드하는 문서다. 새 규칙을 만들 때는 먼저 `src/styles/global.css`, `BaseLayout.astro`, 기존 페이지/컴포넌트에서 같은 역할의 패턴이 있는지 확인한다. 문서와 구현이 충돌하면 구현을 확인한 뒤 문서를 갱신하거나, 의도적인 디자인 변경으로 구현을 함께 수정한다.
