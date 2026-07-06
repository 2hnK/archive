---
type: Agent Instructions
title: AGENTS.md
description: DevArchive에서 AI 에이전트가 따라야 하는 작업, 문서, 디자인 규칙.
tags: ["agent", "instructions", "design", "documentation"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# AGENTS.md

## Role

이 프로젝트에서 AI 에이전트는 기존 SSR 페이지의 디자인 방향성과 HTML/CSS 구조를 기준으로 삼아, 새 요소를 만들 때도 기존 스타일과 규칙을 우선 활용해 통일감 있게 확장하는 보조 개발자 역할을 한다.

## Required Reading

작업 전 다음 문서를 순서대로 확인한다.

1. README.md
2. docs/overview.md
3. docs/project-structure.md
4. docs/development-guide.md
5. docs/knowledge-format.md
6. docs/harness-engineering.md
7. docs/git-conventions.md
8. docs/design/README.md
9. docs/design/design-principles.md
10. docs/design/visual-language.md
11. docs/design/components.md
12. docs/design/do-and-dont.md

## Design Consistency Rules

- 새 UI를 만들기 전에 기존 페이지에서 유사한 레이아웃, 카드, 버튼, 태그, 헤더 패턴이 있는지 먼저 확인한다.
- 기존 패턴으로 해결할 수 있으면 같은 클래스 조합, 여백, 곡률, 타이포그래피 위계를 우선 사용한다.
- 새로운 색상이나 시각적 강조가 필요하면 먼저 `docs/design/color-system.md`의 기존 변수와 상태색으로 해결할 수 있는지 확인한다.
- 기존 패턴으로 부족한 경우에는 현재 디자인 톤과 어울리는 범위에서 새 변형을 만들 수 있다.
- 새 변형을 만들 때는 기존 `glass-panel`, `glass-pill`, `custom-glass-highlight`, `editorial-list`, `reveal-up`, `prose`의 역할과 시각 언어를 참고한다.
- 페이지마다 독립적인 스타일을 만들기보다, 기존 에디토리얼/글래스/고대비 방향 안에서 화면 목적에 맞게 조정한다.
- 애니메이션과 장식 요소는 기존 hover, opacity, translate, scale, sliding highlight 흐름과 자연스럽게 이어지도록 설계한다.
- 큰 제목은 세리프 기반의 에디토리얼 톤을 우선하고, 메타 정보와 UI 라벨은 작은 산세리프 대문자 스타일을 우선 검토한다.

## Code Modification Rules

- 기존 클래스명은 이유 없이 변경하지 않는다.
- 전체 CSS를 대규모로 재작성하기보다 필요한 범위의 스타일을 좁게 추가하거나 확장한다.
- 중복 스타일이 생기지 않도록 기존 유틸리티와 컴포넌트 스타일을 우선 확인한다.
- 새 섹션은 가능한 한 기존 섹션 구조와 네이밍 흐름을 따른다.
- 반응형 레이아웃을 깨뜨리지 않는다.
- 스타일 변경 시 영향 범위를 최소화한다.
- 공통 디자인 토큰은 `src/main/resources/styles/global.css`의 CSS 변수와 컴포넌트 레이어를 우선 확인한다.
- Spring MVC 컨트롤러, Thymeleaf 템플릿, 파일 기반 콘텐츠 서비스 흐름을 기본 전제로 작업한다.

## Documentation Rules

- `README.md`에는 상세 설명을 길게 추가하지 않는다.
- 상세한 정책, 디자인 규칙, 개발 가이드는 `docs/` 하위 문서에 작성한다.
- 디자인 관련 변경사항이 생기면 `docs/design/` 하위 문서도 함께 갱신한다.
- 중요한 설계 결정은 `docs/decisions/` 하위에 기록한다.
- 문서는 현재 구현을 기준으로 작성하되, 새 패턴을 추가한 경우에는 왜 기존 스타일의 자연스러운 확장인지 함께 기록한다.

## New Page And Component Rules

- 새 페이지는 `templates/layout/base.html`의 공통 레이아웃 fragment를 기본으로 사용한다.
- 상단 여백은 고정 내비게이션과 충돌하지 않도록 기존 `pt-[18vh]`, `pt-[20vh]`, `pt-32` 계열을 참고한다.
- 콘텐츠 중심 폭은 본문형 페이지에서 `max-w-[900px]`, 넓은 인덱스 페이지에서 `max-w-[1700px]` 또는 `max-w-7xl` 계열을 먼저 검토한다.
- 카드형 콘텐츠는 `glass-panel`과 기존 반경 계열을 먼저 검토하고, 태그/필터/토글은 `glass-pill` 계열을 먼저 검토한다.
- 목록형 콘텐츠는 `editorial-list`와 `editorial-list-item` 패턴이 맞는지 우선 판단한다.
- 새 인터랙션은 기존 hover, opacity, translate, scale, sliding highlight 흐름과 같은 속도감과 밀도를 유지한다.
- 기존 패턴으로 표현하기 어려운 새 기능은 현재 디자인 원칙을 유지하는 선에서 새 구조를 만들 수 있다.

## Verification Checklist

- 기존 페이지와 새 수정사항의 디자인 톤이 일치하는가?
- 카드, 버튼, 태그, 헤더의 스타일이 기존 규칙과 일관적인가?
- 반응형 레이아웃이 깨지지 않는가?
- 불필요한 중복 CSS가 추가되지 않았는가?
- README와 docs 문서의 규칙을 위반하지 않았는가?
- 새로 추가한 UI가 `docs/design` 문서의 원칙과 맞는가?
- 라이트/다크 모드에서 배경, 텍스트, 보더, 강조색 대비가 유지되는가?
- 문서 변경 시 `npm run docs:validate`가 성공하는가?
- 전체 변경 시 `npm run verify`가 성공하는가?

## Avoid

- 기존 디자인 톤과 무관한 방향으로 전체 스타일을 바꾸는 변경
- 단순 취향에 따른 리디자인
- 기존 클래스명을 이유 없이 바꾸는 변경
- 기존 패턴을 검토하지 않고 별도 디자인 시스템이나 UI 라이브러리를 도입하는 변경
- 현재 프로젝트의 Spring SSR 구조를 필요 없이 다른 프레임워크 구조로 바꾸는 변경
- 고정 내비게이션, 에디토리얼 타이포그래피, 글래스 카드, 다크 모드 변수 구조를 대체 근거 없이 제거하는 변경
- 문서만 필요한 작업에서 HTML/CSS까지 함께 바꾸는 변경
