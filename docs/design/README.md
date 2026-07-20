---
type: Design System Index
title: Design System
description: DevArchive 디자인 시스템 문서의 읽기 순서와 반복 UI 패턴.
tags: ["design", "index", "visual-language"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# Design System

이 문서는 DevArchive의 현재 구현에서 반복적으로 사용되는 디자인 규칙을 정리한 인덱스다. 새 디자인을 제안하기보다 이미 구현된 정적 페이지의 공통 기준을 추출한다.

## Read Order

1. [Design Principles](design-principles.md)
2. [Visual Language](visual-language.md)
3. [Layout System](layout-system.md)
4. [Typography](typography.md)
5. [Color System](color-system.md)
6. [Spacing, Radius, Shadow](spacing-radius-shadow.md)
7. [Components](components.md)
8. [Page Patterns](page-patterns.md)
9. [Do and Don't](do-and-dont.md)

## Implementation Sources

- `src/styles/global.css`: 색상 변수, 글래스 유틸리티, prose, reveal, editorial list의 기준
- `src/layouts/BaseLayout.astro`: 전역 폰트, 테마, 내비게이션, 푸터 구조
- `src/components/Navbar.astro`: 고정 글래스 내비게이션과 sliding highlight
- `src/components/ArticleCard.astro`: 아티클 카드 hover와 이미지 처리
- `src/components/TopicsSidebar.astro`: 카테고리 계층, active state, blue 상태색
- `src/components/TimeProgress.astro`: 도구형 진행 위젯의 제한적 상태색 예외
- `src/components/Footer.astro`: 화면 폭 전체의 얇은 글래스 footer band
- `src/pages/about.astro`: 통합 glass register, sticky rail, 현재 섹션 강조의 기준 페이지
- `src/components/react-bits/`: About에서만 사용하는 제한적 interaction island

## Core Keywords

- 에디토리얼
- 아카이브
- 고대비
- 세리프 중심 제목
- 산세리프 UI 라벨
- 글래스모피즘 패널
- 통합 패널과 내부 hairline
- 둥근 pill 인터랙션
- 얇은 보더
- 절제된 블루 포인트 컬러
- 짧고 절제된 reveal 모션

## Repeated UI Patterns

- 고정 글래스 내비게이션
- 큰 세리프 히어로 제목
- 작은 대문자 메타 라벨
- `glass-panel` 카드
- 단일 패널 안의 register/directory 구획
- `glass-pill` 태그와 토글
- `editorial-list` 기반 목록
- `reveal-up` 스크롤 진입 애니메이션
- 900px 중심 본문과 좌우 사이드바
- sticky section rail과 현재 섹션 번호 강조
- 화면 폭 전체의 낮은 footer band
