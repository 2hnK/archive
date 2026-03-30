---
title: "Next.js App Router 1년 사용기"
description: "Page Router에서 App Router로의 마이그레이션이 가져다 준 변화와 고통"
category: "Frontend"
subcategory: "Next.js"
date: 2026-03-27
tags: ["Next.js", "App Router", "SSR"]
---
Next.js 13 버전부터 전면 도입된 App Router. 1년이라는 시간 동안 실무 환경에서 이를 사용해보며 느꼈던 장점과 뼈아픈 러닝 커브를 가감 없이 회고해 봅니다.

## 서버 컴포넌트(RSC)의 패러다임 전환
클라이언트 컴포넌트 바운더리를 설정하는 과정은 생각보다 혼란스럽습니다. 언제 상태를 내려주고 어떻게 서버에서 데이터를 미리 끌어올 것인지에 대한 설계 고민이 기존 Page Router 시절보다 훨씬 더 치열해졌습니다. 하지만 결국 Layout의 중첩과 스트리밍(Streaming) 렌더링이 주는 UX 향상은 포기할 수 없는 과실이었습니다.
