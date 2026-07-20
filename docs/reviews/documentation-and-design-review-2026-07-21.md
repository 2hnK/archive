---
type: Review Report
title: 문서와 디자인 정합성 검토 기록 2026-07-21
description: About과 Footer 개편 이후 구현, 디자인 문서, 에이전트 정책을 다시 맞춘 검토 보고.
tags: ["review", "documentation", "design", "agent-policy"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# 문서와 디자인 정합성 검토 기록 2026-07-21

## 검토 범위

- `AGENTS.md`, `README.md`
- `docs/overview.md`, 구조·개발·하네스·Git 정책 문서
- `docs/design/*.md`
- 디자인 방향과 React island 결정 기록
- `src/styles/global.css`, `BaseLayout.astro`, 공통 컴포넌트
- Home, Articles, Projects, About의 현재 페이지 구조

## 결론

현재 기준은 에디토리얼 타이포그래피, 절제된 글래스모피즘, 고대비 라이트·다크 테마, 제한적인 블루 accent다. About은 통합 glass register/directory와 현재 섹션 강조를 보여주는 기준 페이지이며, Footer는 큰 카드가 아니라 화면 폭 전체에 맞닿는 낮은 글래스 밴드다.

기존 문서에 남아 있던 red accent, 느린 reveal, `max-w-4xl` About 폭, 모든 글래스 표면을 둥근 카드로 보는 설명은 현재 구현과 맞지 않아 갱신했다.

## 확정한 디자인 기준

- 반복 데이터는 작은 카드를 여러 개 만들기보다 하나의 패널 안에서 hairline으로 나눈다.
- blue accent는 현재 상태, hairline, 링크와 작은 hover에 제한한다.
- 스크롤 상태는 현재 항목 하나만 파란색으로 표시한다.
- 기술 스택과 자격 로고는 식별성을 위해 브랜드 원색을 상시 표시할 수 있다.
- hover는 색상, opacity, hairline, 1~2px 이동 또는 약 1% 확대를 기준으로 한다.
- 흔들림, 반복 반짝임, 강한 glare와 불필요한 3D 효과는 사용하지 않는다.
- React Bits는 About의 `BlurText`, `AnimatedContent` island로 제한한다.
- Footer는 전체 폭, 무곡률, 낮은 높이, 상단 hairline을 사용한다.

## 에이전트 정책 정비

- 모든 문서를 무조건 읽는 목록 대신 기본 문서와 작업별 추가 읽기 경로를 구분했다.
- 사용자 요청, 저장소 규칙, 문서·결정 기록, 현재 구현 순으로 판단 기준을 명시했다.
- 수정 전 dirty worktree와 가장 가까운 구현을 확인하도록 규정했다.
- UI 변경은 실제 로컬 라우트에서 라이트·다크, 반응형, hover/focus, 스크롤 상태를 확인하도록 했다.
- 변경 유형별로 갱신해야 할 디자인·구조·정책 문서를 명시했다.
- 과거 검토 보고서는 수정하지 않고 날짜가 있는 새 보고서로 누적하도록 했다.

## 구현 기준 파일

- `src/styles/global.css`: 전역 토큰, About register/directory, reveal, Footer 상호작용
- `src/pages/about.astro`: hero, sticky rail, section active state, 통합 정보 패널
- `src/components/react-bits/`: 제한적 React interaction island
- `src/components/Footer.astro`: 전체 폭 footer band
- `src/components/Navbar.astro`, `TopicsSidebar.astro`: sliding highlight와 active state
- `src/components/ArticleCard.astro`: 글래스 카드와 이미지 hover

## 검증 기준

- `npm run docs:validate`
- `npm run verify`
- 로컬 About/Footer 라이트 모드 시각 확인
- 기존 Astro 검사 힌트는 실패와 구분해 보고

## 검증 결과

- `npm run docs:validate`: 통과, 29개 Markdown 문서 확인
- `npm run verify`: 통과, 11개 정적 페이지 빌드
- `astro check`: 오류 0건, 기존 비차단 힌트 21건
- About/Footer 로컬 라이트 모드: 통합 패널, 현재 섹션 강조, 전체 폭 Footer 배치 확인
