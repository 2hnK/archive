---
type: Architecture Decision Record
title: 001. Preserve Current Editorial Glass Archive Direction
description: DevArchive의 에디토리얼 글래스 아카이브 디자인 방향을 유지하기로 한 결정.
tags: ["decision", "design", "editorial", "glass"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# 001. Preserve Current Editorial Glass Archive Direction

## Status

Accepted

## Context

현재 프로젝트는 Astro 기반 정적 사이트이며, 이미 홈, 아티클, 프로젝트, 소개 페이지 전반에 공통 디자인 언어가 적용되어 있다. 반복되는 핵심 요소는 세리프 기반 에디토리얼 제목, 고대비 라이트/다크 테마, 절제된 블루 accent, 글래스 패널, pill형 필터, 얇은 border, 짧고 제한적인 reveal animation이다.

## Decision

앞으로의 문서와 구현은 현재 적용된 "editorial glass archive" 방향을 기준으로 유지한다.

새로운 디자인 시스템으로 전면 교체하지 않고, `src/styles/global.css`의 변수와 기존 컴포넌트 패턴을 우선 확장한다. 기존 시각 언어를 유지하는 소규모 인터랙션 island는 [003 결정 기록](003-selective-react-bits-islands.md)의 제한 안에서 사용할 수 있다.

관련 기록은 작은 카드를 반복하기보다 하나의 글래스 패널과 내부 hairline으로 묶는 방식을 우선한다. About의 register/directory를 이 패턴의 기준으로 삼고, Footer는 화면 폭 전체에 맞닿는 낮은 밴드형 예외로 유지한다.

## Consequences

- 새 페이지는 기존 페이지 패턴 중 가까운 구조를 재사용한다.
- 디자인 변경은 현재 톤을 보존하는 범위에서만 수행한다.
- README는 문서 인덱스로 유지하고, 상세 규칙은 `docs/` 아래에서 관리한다.
- AI 에이전트는 작업 전 `AGENTS.md`와 디자인 문서를 읽고 기존 구조를 우선한다.

## Non Goals

- 전체 리디자인
- 기존 디자인 시스템을 대체하는 UI 라이브러리 전면 도입
- 프레임워크 전환
- 페이지별 독립 테마 구성
