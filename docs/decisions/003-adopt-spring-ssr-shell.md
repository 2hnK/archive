---
type: Decision Record
title: Spring SSR Shell 전환
description: Astro 정적 페이지를 Spring Boot와 Thymeleaf 기반 SSR 셸로 전환한 결정 기록.
tags: ["decision", "spring", "thymeleaf", "ssr"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# Spring SSR Shell 전환

## Context

DevArchive는 기존 Astro 정적 페이지에서 Spring Boot 기반 SSR 구조로 전환한다. 목적은 기존 에디토리얼/글래스 디자인과 현재 구현된 화면을 유지하면서, 이후 백엔드 도메인, DB, 관리자 기능을 직접 연습하며 붙일 수 있는 구조를 마련하는 것이다.

## Decision

- Spring Boot와 Thymeleaf를 기본 SSR 구조로 사용한다.
- 기존 공개 화면은 Thymeleaf 템플릿과 fragment로 이식한다.
- 백엔드 도메인 구현은 아직 추가하지 않는다.
- 현재 아티클과 프로젝트는 파일 기반 리소스 서비스로 읽어 화면을 렌더링한다.
- Tailwind CSS는 Astro/Vite 대신 Tailwind CLI와 Gradle 태스크로 생성한다.

## Consequences

- 컨트롤러, 서비스, 템플릿의 기본 경계가 생겨 이후 DB 기반 콘텐츠 관리로 교체하기 쉽다.
- 현재 단계에서는 파일 기반 콘텐츠가 임시 저장소 역할을 하므로 영속성, 인증, 관리자 작성 흐름은 별도 구현 대상이다.
- 디자인 시스템은 기존 CSS 변수, 글래스 패널, pill, editorial list, reveal motion을 그대로 유지한다.
- 검증 기준은 `npm run verify`로 문서 검증과 Spring Boot 빌드를 함께 확인하는 방식으로 바뀐다.
