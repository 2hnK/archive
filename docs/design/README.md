---
type: Design System Index
title: Design System
description: DevArchive 디자인 시스템 문서의 읽기 순서와 반복 UI 패턴.
tags: ["design", "index", "visual-language"]
timestamp: "2026-07-06T00:00:00+09:00"
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

- `src/main/resources/styles/global.css`: 색상 변수, 글래스 유틸리티, prose, reveal, editorial list의 기준
- `src/main/resources/templates/layout/base.html`: 전역 폰트, 테마, 내비게이션, 푸터 구조
- `src/main/resources/templates/fragments/navbar.html`: 고정 글래스 내비게이션과 sliding highlight
- `src/main/resources/templates/fragments/article-card.html`: 아티클 카드 hover와 이미지 처리
- `src/main/resources/templates/fragments/topics-sidebar.html`: 카테고리 계층, active state, blue 상태색

## Core Keywords

- 에디토리얼
- 아카이브
- 고대비
- 세리프 중심 제목
- 산세리프 UI 라벨
- 글래스모피즘 패널
- 둥근 pill 인터랙션
- 얇은 보더
- 레드 포인트 컬러
- 느린 reveal 모션

## Repeated UI Patterns

- 고정 글래스 내비게이션
- 큰 세리프 히어로 제목
- 작은 대문자 메타 라벨
- `glass-panel` 카드
- `glass-pill` 태그와 토글
- `editorial-list` 기반 목록
- `reveal-up` 스크롤 진입 애니메이션
- 900px 중심 본문과 좌우 사이드바
