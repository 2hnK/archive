---
type: Design Guardrails
title: Do And Avoid
description: DevArchive UI를 확장할 때 지켜야 할 디자인 규칙과 피해야 할 변경.
tags: ["design", "guardrails", "review"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# Do And Avoid

## Do

- 기존 `BaseLayout.astro`와 전역 디자인 토큰을 먼저 확인한다.
- `glass-panel`, `glass-pill`, `custom-glass-highlight` 같은 기존 패턴이 새 요소에 맞는지 먼저 검토한다.
- 큰 제목은 세리프 기반 에디토리얼 톤을 우선 검토한다.
- 메타 정보는 작고 조밀한 대문자 라벨 스타일을 우선 검토한다.
- 카드, 목록, 필터, 목차는 기존 hover/active 패턴을 참고해 만든다.
- 새 페이지는 기존 page pattern 중 가장 가까운 것을 선택해 확장하거나, 기존 패턴을 조합해 새 구조를 만든다.
- 기존 패턴으로 부족한 경우에는 현재 톤과 연결되는 새 변형을 만들 수 있다.
- 새 컴포넌트를 만들면 `docs/design/components.md` 또는 `docs/design/page-patterns.md`에 기준을 갱신한다.
- 변경 후 라이트/다크 모드와 모바일/데스크톱을 확인한다.

## Avoid

- 기존 아카이브/에디토리얼/글래스 톤과 연결되지 않는 전체 리디자인
- 페이지마다 별도 컬러 팔레트를 만드는 방식
- 기존 클래스명을 단순 취향으로 변경하는 방식
- `global.css`를 한 번에 크게 갈아엎는 방식
- 카드 안에 카드를 반복해서 넣어 구조를 불필요하게 복잡하게 만드는 방식
- 기존 모션 밀도와 맞지 않는 과도한 애니메이션, 3D 효과, 장식 배경
- 기존 패턴으로 충분한데 새 프레임워크나 UI 라이브러리를 도입하는 방식
- 정적 Astro 페이지 구조를 필요 없이 SPA 중심 구조로 바꾸는 방식

## New Page Checklist

- `BaseLayout.astro`를 사용했는가?
- 상단 고정 nav와 겹치지 않는가?
- 제목, subtitle, meta 라벨이 기존 타이포그래피와 맞는가?
- 카드 또는 목록 패턴을 기존 규칙에서 먼저 검토했는가?
- 색상은 기존 변수와 보조 상태색으로 먼저 해결해 보았는가?
- hover와 reveal motion이 기존 속도와 방향성과 자연스럽게 이어지는가?
- 모바일에서 1열 또는 chip/sidebar 전환이 자연스러운가?
