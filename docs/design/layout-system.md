---
type: Design Reference
title: Layout System
description: DevArchive의 전역 레이아웃, 페이지 여백, 폭 제한, 반응형 규칙.
tags: ["design", "layout", "responsive"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# Layout System

## Global Layout

`BaseLayout.astro`는 고정 내비게이션, 페이지 콘텐츠, 푸터를 포함한다. 본문은 `flex-grow z-10 relative` 컨테이너 안에서 렌더링된다.

Footer는 일반 카드의 중심 폭을 따르지 않고 화면 폭 전체에 맞닿는다. 내부 콘텐츠만 `max-w-[1700px]`로 제한한다.

## Page Top Spacing

고정 내비게이션과 충돌하지 않도록 페이지 상단에는 충분한 여백을 둔다.

- 홈: 모바일 `pt-32`, 데스크톱 `pt-56`
- 프로젝트 상세: `pt-[18vh]`
- 아티클 상세: `pt-32`
- 도구형 페이지: `pt-28` 또는 명시적 상단 여백

## Widths

- 본문 중심 영역: `max-w-[900px]`
- 넓은 인덱스/3열 페이지: `max-w-[1700px]`
- 일반 섹션: `max-w-7xl` 또는 `max-w-[1400px]`
- About hero: `max-w-4xl`
- About register/directory 섹션: `max-w-6xl`
- Footer 내부: `max-w-[1700px]`

## Repeated Layouts

- 홈: 야간 사진 위의 개인 기술 블로그 히어로 뒤에 최신 아티클과 대표 프로젝트를 각각 2열 카드로 배치하는 진입 화면
- 아티클 목록: 좌측 토픽, 중앙 콘텐츠, 우측 여백의 3열 구조
- 아티클 상세: 좌측 토픽, 중앙 본문 카드, 우측 목차
- 프로젝트 목록: 세로 카드 리스트
- 프로젝트 상세: 큰 헤더, 미디어 프레임, 사이드 메타와 본문 12열 구조
- 소개: 통합 hero glass, 220px sticky rail, 단일 패널 내부의 milestone register·tech directory·credential register

## Responsive Rules

- `xl` 미만에서는 아티클 사이드바를 숨기고 모바일 카테고리 chip을 사용한다.
- 카드와 목록은 모바일에서 1열을 기본으로 한다.
- About hero와 section rail은 모바일에서 한 열로 쌓는다. 모바일 section rail은 고정 내비게이션 아래의 낮은 sticky 헤더로 유지해 현재 섹션 번호를 콘텐츠 탐색 중에도 확인할 수 있게 하고, Tech Specs directory는 1열에서 시작해 2열·3열로 확장한다.
- Footer는 모바일에서 브랜드, Navigation, Contact를 세로로 쌓고 데스크톱에서는 한 행에 배치한다.
- 홈의 최근 글 목록은 모바일에서 메타와 읽기 링크를 별도 행으로 쌓아 제목과 설명 폭을 확보한다.
- 텍스트는 `break-keep`, `line-clamp`, 적절한 `leading`으로 한국어와 영어가 섞인 문장을 안정화한다.
- 고정 내비게이션이 있는 페이지는 첫 섹션 top padding을 문서화된 기존 범위에서 먼저 선택한다.
