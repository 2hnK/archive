---
type: Design Reference
title: Spacing, Radius, Shadow
description: DevArchive의 여백, 곡률, 그림자 사용 범위와 재사용 규칙.
tags: ["design", "spacing", "radius", "shadow"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# Spacing, Radius, Shadow

## Spacing

현재 페이지는 큰 상하 여백과 조밀한 내부 UI가 공존한다.

- 페이지 상단: `pt-[20vh]`, `pt-[18vh]`, `pt-[16vh]`, `pt-56`, `pt-32`, `pt-28`
- 페이지 하단: `pb-24`, `pb-32`
- 큰 섹션 간격: `mb-24`, `mb-32`, `md:mb-48`, `mt-32`
- 카드 내부: `p-6`, `md:p-10`, `p-10`, `md:p-14`
- 작은 UI 간격: `gap-1`, `gap-2`, `gap-3`
- 콘텐츠 카드/목록 간격: `gap-8`, `gap-12`, `gap-24`

## Radius

전역 테마의 기본 radius는 0에 가깝지만, 실제 UI는 글래스 카드와 pill에서 큰 곡률을 사용한다.

- pill: `rounded-full`
- 글래스 하이라이트: `rounded-[1.2rem]`
- 아티클 피드 카드: `rounded-[2.5rem]`
- 프로젝트 상세 미디어: `rounded-[2.2rem]`, `md:rounded-[3rem]`
- 일반 도구형 입력: `rounded-lg`, `rounded-xl`

## Shadow

- 글래스 패널은 `box-shadow`와 inset highlight로 깊이를 만든다.
- 프로젝트 상세 미디어는 큰 그림자(`shadow-[0_30px_70px_-15px_rgba(...)]`)를 사용한다.
- 작은 카드나 도구형 UI는 `shadow-sm`, hover 시 `shadow-md` 수준을 사용한다.

## Rules

- 새 radius scale을 만들기보다 기존 범위를 재사용한다.
- 글래스 카드에는 border, blur, shadow가 함께 있어야 한다.
- 그림자를 과하게 늘려 카드가 떠 보이는 방향으로 바꾸지 않는다.
- 카드 안에 다시 카드형 섹션을 중첩하기보다 목록, hairline, pill, 내부 구분선으로 밀도를 조절한다.
