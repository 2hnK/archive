---
type: Design Reference
title: Layout System
description: DevArchive의 전역 레이아웃, 페이지 여백, 폭 제한, 반응형 규칙.
tags: ["design", "layout", "responsive"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# Layout System

## Global Layout

`BaseLayout.astro`는 고정 내비게이션, 페이지 콘텐츠, 푸터를 포함한다. 본문은 `flex-grow z-10 relative` 컨테이너 안에서 렌더링된다.

## Page Top Spacing

고정 내비게이션과 충돌하지 않도록 페이지 상단에는 충분한 여백을 둔다.

- 홈: `pt-[20vh]`
- 프로젝트 상세: `pt-[18vh]`
- 아티클 상세: `pt-32`
- 도구형 페이지: `pt-28` 또는 명시적 상단 여백

## Widths

- 본문 중심 영역: `max-w-[900px]`
- 넓은 인덱스/3열 페이지: `max-w-[1700px]`
- 일반 섹션: `max-w-7xl` 또는 `max-w-[1400px]`
- 소개/스펙 섹션: `max-w-4xl`

## Repeated Layouts

- 홈: 큰 히어로 후 2열 editorial list
- 아티클 목록: 좌측 토픽, 중앙 콘텐츠, 우측 여백의 3열 구조
- 아티클 상세: 좌측 토픽, 중앙 본문 카드, 우측 목차
- 프로젝트 목록: 세로 카드 리스트
- 프로젝트 상세: 큰 헤더, 미디어 프레임, 사이드 메타와 본문 12열 구조
- 소개: 중앙 히어로, 타임라인, 기술 그리드, 인증 리스트

## Responsive Rules

- `xl` 미만에서는 아티클 사이드바를 숨기고 모바일 카테고리 chip을 사용한다.
- 카드와 목록은 모바일에서 1열을 기본으로 한다.
- 텍스트는 `break-keep`, `line-clamp`, 적절한 `leading`으로 한국어와 영어가 섞인 문장을 안정화한다.
- 고정 내비게이션이 있는 페이지는 첫 섹션 top padding을 문서화된 기존 범위에서 먼저 선택한다.
