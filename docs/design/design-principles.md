---
type: Design Principles
title: Design Principles
description: DevArchive의 에디토리얼 글래스 아카이브 디자인 원칙.
tags: ["design", "principles", "editorial", "glass"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# Design Principles

## Extend From The Archive Tone

DevArchive는 제품 랜딩 페이지보다 개인 개발 아카이브에 가깝다. 화면은 설명을 과하게 늘어놓기보다 제목, 기록, 목록, 본문을 명확하게 보여준다.

새 요소를 만들 때는 이 톤을 고정된 규칙으로 묶기보다, 기존 화면에서 반복된 스타일을 출발점으로 삼아 자연스럽게 확장한다.

## Editorial First

큰 제목은 영문 `Newsreader`와 한글 `Noto Serif KR` 기반 세리프로 에디토리얼 인상을 만들고, 본문과 UI 조작 요소는 영문 `Manrope`와 한글 `Noto Sans KR` 기반 산세리프로 정리한다.

## High Contrast With Restrained Accent

기본 색은 흰색/검정 또는 다크 배경/크림 텍스트다. 강조와 상태 표시는 절제된 블루 계열 `--accent-color`를 우선 사용한다. 넓은 색면보다 hairline, 작은 라벨, 링크와 hover 반응에 제한해 사용하며, 새 색상이 필요하면 기존 변수와 조화를 이루는지 먼저 확인한다.

## Glass As Container

주요 카드와 내비게이션은 반투명 배경, blur, 얇은 보더, 내부 하이라이트를 사용한다. 글래스 효과는 장식이 아니라 콘텐츠 그룹을 구분하는 컨테이너 역할이다.

관련 항목이 반복될 때는 작은 글래스 카드를 여러 개 만드는 대신 하나의 패널 안에서 hairline으로 구획하는 방식을 먼저 검토한다. About의 Milestones, Tech Specs, Certifications가 이 패턴의 기준이다.

## Motion Is Restrained And Purposeful

진입 애니메이션은 `reveal-up`처럼 짧은 opacity와 translate 흐름을 우선 참고한다. hover는 color, opacity, hairline, 1~2px 이동 또는 약 1% 확대처럼 결과를 방해하지 않는 범위에서 사용한다. 흔들림, 반복 반짝임, 큰 glare는 사용하지 않는다.

현재 위치를 알려야 하는 상호작용에서는 여러 항목을 동시에 강조하지 않는다. About의 섹션 번호처럼 현재 스크롤 상태만 blue accent로 표시하고 나머지는 중립 상태를 유지한다.

## Static Structure First

이 프로젝트는 정적 HTML/CSS/Astro 기반 사이트다. 디자인 일관성을 위해 현재 구조를 기본값으로 삼고, 큰 구조 변경이나 UI 라이브러리 도입은 명확한 필요가 있을 때만 검토한다.

## Implementation Is The Source

디자인 문서는 구현을 설명하고 가이드하는 문서다. 새 규칙을 만들 때는 먼저 `src/styles/global.css`, `BaseLayout.astro`, 기존 페이지/컴포넌트에서 같은 역할의 패턴이 있는지 확인한다. 문서와 구현이 충돌하면 구현을 확인한 뒤 문서를 갱신하거나, 의도적인 디자인 변경으로 구현을 함께 수정한다.
