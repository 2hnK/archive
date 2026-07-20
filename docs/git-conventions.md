---
type: Git Convention
title: Git 컨벤션과 작업 규칙
description: DevArchive의 브랜치, 커밋, 검증, PR 작성 기준.
tags: ["git", "commit", "workflow", "quality"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# Git 컨벤션과 작업 규칙

## 기본 원칙

- 커밋은 하나의 논리적 변경 단위로 나눈다.
- 문서, 하네스, UI 변경은 가능하면 별도 커밋으로 분리한다.
- `node_modules/`, `dist/`, `.astro/`, `.env`, `.dump/`는 커밋하지 않는다.
- 이미 존재하는 사용자 변경은 되돌리지 않는다.
- 변경 전후 검증 명령과 결과를 작업 보고에 남긴다.

## 브랜치 이름

형식:

```text
<type>/<short-topic>
```

권장 type:

- `feat`: 사용자 기능 또는 새 페이지
- `fix`: 버그 수정
- `docs`: 문서 변경
- `chore`: 설정, 하네스, 유지관리
- `refactor`: 동작 변경 없는 구조 개선

예시:

```text
docs/okf-harness
chore/doc-validation
fix/article-filter-state
```

## 커밋 메시지

형식:

```text
<type>(<scope>): <요약>
```

scope는 선택 사항이다.

권장 type:

- `feat`: 새 기능
- `fix`: 버그 수정
- `docs`: 문서 변경
- `style`: 포맷 또는 시각 표현만 변경
- `refactor`: 동작 변경 없는 코드 구조 개선
- `test`: 테스트나 검증 보강
- `chore`: 빌드, 설정, 도구, 의존성 관리
- `build`: 빌드 시스템 변경
- `ci`: CI 구성 변경
- `perf`: 성능 개선
- `revert`: 이전 커밋 되돌림

예시:

```text
docs(okf): 문서 frontmatter 규칙 추가
chore(harness): 문서 검증 스크립트 추가
docs(design): 공통 컴포넌트 기준 보강
```

## 커밋 전 검증

기본 검증:

```sh
npm run verify
```

문서만 변경한 경우에도 최소한 다음을 실행한다.

```sh
npm run docs:validate
```

UI나 CSS를 변경한 경우에는 `npm run build`와 함께 실제 로컬 라우트에서 라이트/다크 모드, 모바일/데스크톱 폭, 주요 hover/focus와 스크롤 상태를 확인한다.

## 커밋 본문

커밋 본문은 필요할 때만 작성한다. 작성한다면 다음 정보를 우선한다.

- 변경 이유
- 검증 명령
- 의도적으로 제외한 범위
- 후속 검토가 필요한 리스크

## PR 기준

- PR은 짧은 생명주기를 유지한다.
- 설명에는 변경 요약, 검증 결과, 스크린샷 필요 여부를 적는다.
- 디자인 변경은 `docs/design/` 갱신 여부를 확인한다.
- 문서 정책 변경은 `docs/decisions/`에 결정 기록이 필요한지 확인한다.
