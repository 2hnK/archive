---
type: Agent Instructions
title: AGENTS.md
description: DevArchive에서 AI 에이전트가 따라야 하는 작업, 문서, 디자인 규칙.
tags: ["agent", "instructions", "design", "documentation"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# AGENTS.md

## Role

AI 에이전트는 DevArchive의 정적 Astro 구조와 현재 디자인 언어를 보존하면서 기능, 콘텐츠, 문서를 일관되게 확장한다. 화면을 새로 꾸미는 역할에 그치지 않고 관련 구현과 문서가 같은 사실을 설명하도록 유지하는 보조 개발자 역할을 한다.

## Source Of Truth

판단 우선순위는 다음과 같다.

1. 사용자의 현재 요청
2. 이 `AGENTS.md`의 저장소 규칙
3. 관련 `docs/` 문서와 승인된 결정 기록
4. 현재 동작하는 구현과 가장 가까운 기존 패턴

문서와 구현이 다르면 한쪽을 임의로 따르지 않는다. 관련 코드와 결정 기록을 확인해 현재 의도를 판단하고, 작업 범위 안에서 구현과 문서를 함께 맞춘다.

## Required Reading And Routing

모든 작업의 기본 읽기 순서:

1. `README.md`
2. `docs/overview.md`
3. `docs/project-structure.md`
4. `docs/development-guide.md`
5. `docs/harness-engineering.md`
6. `docs/git-conventions.md`

작업 유형에 따라 다음 문서를 추가로 읽는다.

- UI·CSS·페이지 디자인: `docs/design/README.md`의 읽기 순서와 `docs/decisions/001-design-direction.md`
- React island·React Bits: `docs/decisions/003-selective-react-bits-islands.md`
- 문서 생성·정책 변경: `docs/knowledge-format.md`
- 콘텐츠 컬렉션: `src/content.config.ts`와 가장 가까운 기존 Markdown 콘텐츠

코드나 현재 화면에서 확인할 수 있는 내용은 사용자에게 다시 묻지 않는다. 결과를 크게 바꾸는 모호함만 질문한다.

## Current Design Baseline

- 기본 방향은 에디토리얼 타이포그래피, 절제된 글래스모피즘, 고대비 라이트·다크 테마, 제한적인 블루 accent다.
- 블루는 현재 상태, hairline, 링크, 작은 hover에 사용한다. 큰 배경 면이나 페이지별 독립 팔레트로 확장하지 않는다.
- 관련 항목은 여러 개의 작은 카드보다 하나의 큰 글래스 패널 안에서 내부 hairline으로 나누는 방식을 먼저 검토한다.
- About은 현재 에디토리얼 글래스 페이지의 기준 구현이다. sticky section rail, 현재 섹션만 파란 번호, 통합 register/directory 패턴을 참고한다.
- Footer는 큰 둥근 카드가 아니라 화면 좌우에 맞닿는 낮은 글래스 밴드다.
- React Bits는 About의 `BlurText`, `AnimatedContent` island로 제한한다. 다른 페이지에 확대하려면 기존 CSS 모션으로 해결할 수 없는 이유와 결정 문서 갱신이 필요하다.
- 브랜드·자격 로고는 식별성이 목적이므로 원색을 상시 사용할 수 있다. 일반 UI accent 규칙과 혼동하지 않는다.
- 흔들림, 반복 반짝임, 과한 glare, 큰 3D 변형은 사용하지 않는다. hover는 색상·opacity·hairline과 1~2px 이동 또는 약 1% 확대 수준을 우선한다.

## Design Consistency Rules

- 새 UI를 만들기 전에 기존 페이지에서 유사한 레이아웃, 카드, 버튼, 태그, 헤더 패턴이 있는지 먼저 확인한다.
- 기존 패턴으로 해결할 수 있으면 같은 클래스 조합, 여백, 곡률, 타이포그래피 위계를 우선 사용한다.
- 새로운 색상이나 시각적 강조가 필요하면 먼저 `docs/design/color-system.md`의 기존 변수와 상태색으로 해결할 수 있는지 확인한다.
- 기존 패턴으로 부족한 경우에는 현재 디자인 톤과 어울리는 범위에서 새 변형을 만들 수 있다.
- 새 변형을 만들 때는 기존 `glass-panel`, `glass-pill`, `custom-glass-highlight`, `editorial-list`, `reveal-up`, `prose`의 역할과 시각 언어를 참고한다.
- 페이지마다 독립적인 스타일을 만들기보다, 기존 에디토리얼/글래스/고대비 방향 안에서 화면 목적에 맞게 조정한다.
- `glass-panel`은 콘텐츠를 묶는 표면으로 사용한다. 글래스 카드 안에 같은 위계의 카드를 반복 중첩하지 않는다.
- 애니메이션과 장식 요소는 기존 hover, opacity, 짧은 translate/scale, sliding highlight 흐름과 자연스럽게 이어지도록 설계한다.
- 큰 제목은 세리프 기반의 에디토리얼 톤을 우선하고, 메타 정보와 UI 라벨은 작은 산세리프 대문자 스타일을 우선 검토한다.

## Code Modification Rules

- 수정 전 `git status`와 관련 diff를 확인해 기존 사용자 변경을 보존한다.
- 기존 클래스명은 이유 없이 변경하지 않는다.
- 전체 CSS를 대규모로 재작성하기보다 필요한 범위의 스타일을 좁게 추가하거나 확장한다.
- 중복 스타일이 생기지 않도록 기존 유틸리티와 컴포넌트 스타일을 우선 확인한다.
- 새 섹션은 가능한 한 기존 섹션 구조와 네이밍 흐름을 따른다.
- 반응형 레이아웃을 깨뜨리지 않는다.
- 스타일 변경 시 영향 범위를 최소화한다.
- 공통 디자인 토큰은 `src/styles/global.css`의 CSS 변수와 컴포넌트 레이어를 우선 확인한다.
- Astro 페이지 구조, 콘텐츠 컬렉션 흐름, 정적 라우팅 방식을 기본 전제로 작업한다.
- 개발 서버가 이미 실행 중이면 재사용하고, 시각 변경은 실제 로컬 라우트에서 확인한다.

## Documentation Rules

- `README.md`에는 상세 설명을 길게 추가하지 않는다.
- 상세한 정책, 디자인 규칙, 개발 가이드는 `docs/` 하위 문서에 작성한다.
- 디자인 관련 변경사항이 생기면 `docs/design/` 하위 문서도 함께 갱신한다.
- 중요한 설계 결정은 `docs/decisions/` 하위에 기록한다.
- 문서는 현재 구현을 기준으로 작성하되, 새 패턴을 추가한 경우에는 왜 기존 스타일의 자연스러운 확장인지 함께 기록한다.
- 과거 검토 보고서는 당시 기록으로 남긴다. 새 검토 결과는 날짜가 포함된 새 `docs/reviews/` 문서로 추가한다.

변경별 기본 문서 갱신 범위:

- 전역 색상·모션·표면 규칙: `docs/design/design-principles.md`, `visual-language.md`, 관련 토큰 문서
- 공통 컴포넌트: `docs/design/components.md`
- 페이지 레이아웃: `docs/design/layout-system.md`, `page-patterns.md`
- 의존성·구조·라우트: `docs/project-structure.md`, `development-guide.md`, 필요 시 결정 기록
- 에이전트 흐름·검증 정책: `AGENTS.md`, `docs/harness-engineering.md`, `git-conventions.md`

## New Page And Component Rules

- 새 페이지는 `BaseLayout.astro`를 기본 레이아웃으로 사용한다.
- 상단 여백은 고정 내비게이션과 충돌하지 않도록 기존 `pt-[18vh]`, `pt-[20vh]`, `pt-32` 계열을 참고한다.
- 콘텐츠 중심 폭은 본문형 페이지에서 `max-w-[900px]`, 넓은 인덱스 페이지에서 `max-w-[1700px]` 또는 `max-w-7xl` 계열을 먼저 검토한다.
- 카드형 콘텐츠는 `glass-panel`과 기존 반경 계열을 먼저 검토하고, 관련 데이터가 반복되면 단일 패널+내부 구분선 구조도 함께 검토한다. 태그/필터/토글은 `glass-pill` 계열을 먼저 검토한다.
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
- UI 변경은 실제 라우트에서 데스크톱과 모바일, hover/focus, 스크롤 상태를 확인했는가?
- `prefers-reduced-motion`에서 필수 콘텐츠와 기능이 유지되는가?
- 문서 변경 시 `npm run docs:validate`가 성공하는가?
- 전체 변경 시 `npm run verify`가 성공하는가?

## Avoid

- 기존 디자인 톤과 무관한 방향으로 전체 스타일을 바꾸는 변경
- 단순 취향에 따른 리디자인
- 기존 클래스명을 이유 없이 바꾸는 변경
- 기존 패턴을 검토하지 않고 별도 디자인 시스템이나 UI 라이브러리를 도입하는 변경
- 기존 CSS로 충분한데 React island나 클라이언트 상태를 추가하는 변경
- 현재 프로젝트의 정적 Astro 구조를 필요 없이 다른 프레임워크 구조로 바꾸는 변경
- 고정 내비게이션, 에디토리얼 타이포그래피, 글래스 카드, 다크 모드 변수 구조를 대체 근거 없이 제거하는 변경
- 문서만 필요한 작업에서 HTML/CSS까지 함께 바꾸는 변경
