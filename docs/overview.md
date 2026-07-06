---
type: Project Overview
title: Project Overview
description: DevArchive의 목적, 사용자 흐름, 문서 정책 요약.
tags: ["project", "overview", "spring", "thymeleaf"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# Project Overview

DevArchive는 Spring Boot와 Thymeleaf로 구성된 SSR 개발 아카이브 사이트다. 홈, 아티클 목록/상세, 프로젝트 목록/상세, 소개 페이지, 작성 보조 페이지를 제공한다.

## Purpose

- 개발 기록, 네트워크/엔지니어링 글, 프로젝트 기록을 정적 사이트로 정리한다.
- 콘텐츠는 리소스 디렉터리의 Markdown/HTML 파일과 Spring 서비스, Thymeleaf 템플릿으로 렌더링한다.
- 시각 스타일은 에디토리얼 타이포그래피, 고대비 라이트/다크 테마, 글래스모피즘 카드, 느린 전환 애니메이션을 중심으로 유지한다.

## Current Design Keywords

- Editorial
- Artistic archive
- High contrast
- Glassmorphism
- Serif hero typography
- Minimal monochrome with red accent
- Rounded glass cards
- Small uppercase metadata
- Slow reveal motion
- SSR content first

## Main User Flows

- 홈에서 최신 아티클과 대표 프로젝트로 이동한다.
- 아티클 목록에서 피드/그리드 뷰를 전환하고 카테고리로 필터링한다.
- 아티클 상세에서 본문, 좌측 토픽, 우측 목차를 함께 탐색한다.
- 프로젝트 목록에서 카드형 프로젝트를 확인하고 프로젝트 상세 기록으로 이동한다.
- 소개 페이지에서 이력, 기술 스택, 자격 정보를 확인한다.

## Backend Scope

현재 Spring 전환은 SSR 셸과 화면 렌더링 틀을 잡는 단계다. DB, 인증, 관리자 작성 기능, 도메인 서비스는 이후 연습하면서 직접 구현할 확장 영역으로 남겨 둔다.

## Documentation Policy

`README.md`는 문서 인덱스다. 구조, 개발 절차, 디자인 시스템, Git 규칙, 하네스, 설계 결정은 `docs/` 하위 문서에 둔다.

Git이 추적하는 Markdown 문서는 [OKF 문서 형식](knowledge-format.md)을 따른다. 문서와 빌드 검증은 [하네스 엔지니어링 구성](harness-engineering.md)의 `npm run verify`를 기준으로 한다.
