---
type: Architecture Decision Record
title: 002. OKF와 문서 검증 하네스 채택
description: DevArchive 문서를 OKF 기반 지식 단위로 정리하고 최소 검증 하네스를 도입한 결정.
tags: ["decision", "okf", "harness", "documentation"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# 002. OKF와 문서 검증 하네스 채택

## Status

Accepted

## Context

DevArchive는 정적 Astro 사이트이며, 에이전트가 작업 전 `AGENTS.md`를 통해 `README.md`와 `docs/` 문서를 읽는 구조를 갖고 있다. 기존 문서는 사람이 읽기에는 충분했지만, 문서 유형과 검증 상태를 기계적으로 확인하는 규칙은 없었다.

Google Cloud의 Open Knowledge Format은 Markdown 파일과 YAML frontmatter를 기반으로 지식 단위를 표현한다. OpenAI의 하네스 엔지니어링 글도 큰 지침 파일 대신 구조화된 저장소 지식, 기계적 검증, 에이전트가 읽을 수 있는 피드백 루프를 강조한다.

## Decision

Git이 추적하는 Markdown 문서에 OKF `type` frontmatter를 추가한다.

문서 검증 스크립트 `scripts/validate-docs.mjs`를 추가하고, `npm run verify`가 다음 검증을 순서대로 실행하도록 한다.

```sh
npm run docs:validate
npm run check
npm run build
```

## Consequences

- 새 문서는 `type` 필드를 포함해야 한다.
- 깨진 로컬 문서 링크는 검증 단계에서 실패한다.
- 에이전트는 문서 유형을 기준으로 필요한 지식을 더 쉽게 찾을 수 있다.
- 콘텐츠 컬렉션 문서도 OKF `type` 필드를 가지지만, 사이트 렌더링 스키마와 충돌하지 않도록 Astro 검증을 함께 실행한다.

## Non Goals

- OKF 전체 소비기나 시각화 도구 도입
- 원격 CI/CD 구성 추가
- 대형 관측성 스택 추가
- `.dump/` 로컬 초안 문서의 버전 관리 편입

