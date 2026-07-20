---
type: Project Index
title: DevArchive
description: Astro 기반 정적 개발 아카이브 사이트의 문서 진입점.
tags: ["project", "astro", "documentation"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# DevArchive

DevArchive는 Astro 기반의 정적 개발 아카이브 사이트입니다. 아티클, 프로젝트, 소개 페이지를 에디토리얼 타이포그래피와 글래스모피즘 UI로 구성합니다.

이 README는 긴 설명서가 아니라 프로젝트 문서의 진입점입니다. 상세한 개발 규칙, 구조 설명, 디자인 시스템은 `docs/` 하위 문서를 확인합니다.

## Documents

- [프로젝트 개요](docs/overview.md)
- [프로젝트 구조](docs/project-structure.md)
- [개발 가이드](docs/development-guide.md)
- [OKF 문서 형식](docs/knowledge-format.md)
- [하네스 엔지니어링 구성](docs/harness-engineering.md)
- [Git 컨벤션과 작업 규칙](docs/git-conventions.md)
- [디자인 시스템](docs/design/README.md)
- [디자인 원칙](docs/design/design-principles.md)
- [컴포넌트 규칙](docs/design/components.md)
- [Do and Don't](docs/design/do-and-dont.md)
- [설계 결정 기록](docs/decisions/001-design-direction.md)
- [OKF와 하네스 결정 기록](docs/decisions/002-adopt-okf-and-harness.md)
- [선택적 React Bits island 결정 기록](docs/decisions/003-selective-react-bits-islands.md)
- [문서와 디자인 검토 기록](docs/reviews/documentation-and-design-review-2026-07-06.md)
- [최신 문서와 디자인 정합성 검토](docs/reviews/documentation-and-design-review-2026-07-21.md)

## Start Here

개발자는 먼저 [docs/overview.md](docs/overview.md), [docs/project-structure.md](docs/project-structure.md), [docs/development-guide.md](docs/development-guide.md)를 읽습니다.

AI 에이전트는 작업 전에 [AGENTS.md](AGENTS.md)를 먼저 확인하고, 그 안의 Required Reading 순서를 따릅니다.

## Commands

```sh
npm install
npm run dev
npm run docs:validate
npm run verify
npm run build
npm run preview
```
