---
type: Design Reference
title: Visual Language
description: DevArchive의 시각 톤, 상호작용 특성, 피해야 할 방향.
tags: ["design", "visual-language", "interaction"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# Visual Language

## Tone

현재 디자인은 예술적 개발 아카이브, 에디토리얼 포트폴리오, 기술 기록 저장소의 중간 지점에 있다.

## Visual Characteristics

- 강한 타이포그래피로 첫 인상을 만든다.
- 콘텐츠 영역은 넓게 비워두고 카드와 보더로 그룹을 구분한다.
- UI 라벨은 작고 조밀하며 대문자와 넓은 tracking을 자주 사용한다.
- 글래스 효과는 내비게이션, 카드, 필터, 토글에 반복된다.
- 같은 종류의 기록은 하나의 글래스 표면 안에서 hairline으로 나누어 밀도를 만든다.
- 이미지는 카드 hover나 프로젝트 상세 hero에서 보조적으로 사용한다.
- Footer는 독립적인 둥근 카드가 아니라 화면 좌우에 맞닿는 낮은 글래스 밴드다.

## Interaction Characteristics

- 내비게이션과 토픽 목록은 sliding highlight를 사용한다.
- 리스트 hover는 배경 반전, 좌우 padding 변화, arrow rotation으로 반응한다.
- 카드 hover는 제목 강조색, 이미지 scale, 경계/그림자 변화로 반응한다.
- About의 register/directory hover는 hairline, 옅은 배경, 1~2px 이동만 사용한다.
- 현재 스크롤 섹션 번호만 blue accent로 표시한다.
- 진입 모션은 약 24~32px 이동과 0.85초 안팎의 짧은 흐름을 기준으로 한다.
- 사용자가 모션 감소를 요청하거나 JavaScript를 사용할 수 없는 환경에서는 진입 모션을 생략하고 콘텐츠를 즉시 노출한다.

## Source Patterns

- sliding highlight: `Navbar.astro`, `TopicsSidebar.astro`
- 카드 이미지 scale: `ArticleCard.astro`, 아티클 목록 feed 카드
- reveal motion: `global.css`의 `.reveal-up`
- editorial list hover: `global.css`의 `.editorial-list-item`
- About section state: `about.astro`의 `about-section-active`
- limited React island: `BlurText`, `AnimatedContent`

## Avoid

- 마케팅 랜딩 페이지처럼 과한 설명 블록을 추가하지 않는다.
- 장식용 그래픽, 과한 배경 패턴, 새로운 애니메이션 체계를 추가하지 않는다.
- 흔들림, 반복 반짝임, 강한 glare처럼 콘텐츠보다 먼저 보이는 hover 효과를 추가하지 않는다.
- 페이지마다 독립적인 컬러 테마를 만들지 않는다.
