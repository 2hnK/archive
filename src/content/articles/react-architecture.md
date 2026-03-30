---
title: "현대적인 리액트 아키텍처"
description: "컴포넌트를 어떻게 분리하고 상태를 관리하는 것이 가장 이상적인가?"
category: "Frontend"
subcategory: "React"
date: 2026-03-30
tags: ["React", "Architecture", "State Management"]
---
현대 프론트엔드 환경에서 React 애플리케이션의 규모가 커짐에 따라, 올바른 아키텍처를 잡는 것은 선택이 아닌 필수가 되었습니다. 

이 글에서는 비즈니스 로직과 UI 컴포넌트를 분리하는 관심사의 분리(Separation of Concerns)부터, 전역 상태(Global State)와 서버 상태(Server State)를 명확히 구분하여 다루는 최신 트렌드를 짚어봅니다.

## 1. 컴포넌트의 책임 분리
가장 기본적이면서도 중요한 것은 하나의 컴포넌트가 하나의 책임만 가지도록 하는 것입니다. Container-Presenter 패턴은 여전히 강력하며, 최근에는 Custom Hook을 사용해 로직을 숨기는 패턴이 각광받고 있습니다.

## 2. 서버 상태는 서버로, 클라이언트 상태는 클라이언트로
Redux나 Zustand 하나에 모든 데이터를 때려 박던 시대는 지났습니다. React Query나 SWR 같은 도구를 활용해 서버 데이터를 캐싱하고 관리하면 보일러플레이트 코드를 획기적으로 줄일 수 있습니다.
