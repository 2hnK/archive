---
type: Architecture Decision Record
title: 003. React Bits를 선택적 인터랙션 island로 도입
description: 기존 Astro 정적 구조와 에디토리얼 글래스 디자인을 유지하면서 React Bits 효과를 제한적으로 사용하는 결정.
tags: ["decision", "design", "react", "react-bits", "astro"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# 003. React Bits를 선택적 인터랙션 island로 도입

## Status

Accepted

## Context

DevArchive는 Astro 기반 정적 사이트이며 세리프 타이포그래피, 고대비 색상, 글래스 패널, 절제된 reveal motion을 공통 언어로 사용한다. About의 핵심 제목과 섹션 진입에 제한적인 모션을 더할 필요가 있지만, 사이트 전체를 React 애플리케이션으로 바꾸거나 별도 디자인 시스템을 도입하면 현재 구조와 시각적 일관성을 해칠 수 있다.

## Decision

React Bits의 `BlurText`, `AnimatedContent` 동작을 프로젝트 안의 TypeScript 컴포넌트로 관리한다.

- Astro의 React integration을 추가하되 필요한 컴포넌트만 `client:load` 또는 `client:visible`로 hydration한다.
- 색상, 표면, 곡률, 그림자는 기존 CSS 변수와 에디토리얼 hairline 패턴을 사용한다.
- 효과는 About의 인사말과 정보 섹션 진입으로 범위를 제한한다. Home과 프로필 hover는 Astro 마크업 및 기존 CSS만 사용한다.
- `prefers-reduced-motion`을 존중하고, JavaScript가 없어도 콘텐츠 구조와 링크가 그대로 유지되도록 한다.

## Consequences

- React와 Motion 관련 의존성이 추가되지만 나머지 페이지는 기존 Astro 정적 렌더링을 유지한다.
- 새 효과를 추가하기 전에 기존 두 컴포넌트와 CSS만으로 해결할 수 있는지 먼저 검토한다.
- React island의 server/client 마크업은 결정적이어야 하며, 전역 reveal observer와 함께 사용할 때 hydration 상태를 확인한다.
- 디자인 변경 시 `docs/design/components.md`와 해당 페이지 패턴을 함께 갱신한다.

## Non Goals

- 전체 페이지의 React 전환
- React Bits의 모든 컴포넌트 설치
- 기존 글래스·에디토리얼 디자인 시스템 교체
- 장식 효과만을 위한 대형 WebGL 배경 도입
