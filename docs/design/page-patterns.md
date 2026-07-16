---
type: Design Reference
title: Page Patterns
description: 홈, 아티클, 프로젝트, 소개, 도구형 페이지의 반복 레이아웃 패턴.
tags: ["design", "page-patterns", "layout"]
timestamp: "2026-07-06T00:00:00+09:00"
---

# Page Patterns

## Home

- 개인 기술 블로그임을 먼저 알리는 작은 메타 라벨과 큰 세리프 히어로 문장
- 와이드 개인 사진은 홈의 full-bleed ambient background로 사용하고, 히어로와 다음 섹션 사이의 전환 여백까지 자연스럽게 덮는 높이로 확장
- 사진은 비교적 선명하게 노출하되 하단 단방향 gradient로 목록 진입 전에 배경색에 흡수
- 히어로 타이포그래피와 메타 라벨은 따뜻한 흰색과 깊은 shadow를 사용해 사진 위 대비를 확보
- 히어로 상단 여백과 높이는 viewport 높이 단위 대신 고정 spacing을 사용해 최근 게시물과 프로젝트의 세로 시작점을 일정하게 유지
- accent line으로 시각적 리듬 형성
- 별도 소개 문장과 주제 태그 없이 히어로 다음에 최근 게시물을 바로 배치
- 하단은 최근 게시물과 대표 프로젝트를 동일 비율로 배치한 2열 editorial list

## Articles Index

- 상단의 큰 `Articles` 제목과 feed/grid view toggle은 같은 row에서 하단 정렬
- `xl` 이상: 좌측 토픽 사이드바, 중앙 900px 콘텐츠
- `xl` 미만: 모바일 category chip
- feed view는 큰 `glass-panel` 카드
- grid view는 `ArticleCard` 2열
- 목록 하단은 필터 결과를 기준으로 계산되는 숫자형 페이지네이션 사용

## Article Detail

- 상단 title/meta bar
- 3열 구조: 좌측 topic, 중앙 article card, 우측 TOC
- 본문은 `glass-panel` 안의 `.prose`
- 목차는 sliding highlight와 scroll spy

## Project Index

- 큰 `Projects` 제목
- 프로젝트별 큰 `glass-panel` 카드
- 연도 pill, 제목, 설명, 태그, 원형 arrow action
- hover 시 배경 이미지가 은은하게 드러남

## Project Detail

- back link
- 연도 pill과 초대형 세리프 제목
- 설명은 accent border-left로 강조
- 미디어는 큰 radius와 깊은 shadow
- 하단은 sidebar meta와 prose content의 12열 구조

## About

- 세로형 프로필 사진과 짧은 인용문을 나란히 배치한 editorial hero
- 인용문 위에는 이름을 포함한 짧은 인사말을 두어 페이지의 주체를 명확히 표시
- 모바일에서는 프로필 사진과 인용문을 한 열로 쌓아 인물 구도를 유지
- 은은한 accent glow
- 날짜 축과 본문을 나란히 배치한 단일 세로 editorial timeline
- milestone은 카드보다 hairline과 세리프 제목으로 위계를 만들되, 2px gradient 축과 순번 node로 시간의 흐름을 명확히 표시하고 수상 항목만 badge로 강조
- Tech Specs는 Backend, AI, Frontend, Data, Infra 역할별 행과 흰색 skill chip으로 구성
- border-bottom 기반 인증 리스트

## Tool Pages

`/write`, `/write-project`, `/snippets`는 보조 도구 성격이 강하다. 일부 zinc 계열, rounded input, form UI가 사용되지만, 공개 아카이브 페이지의 핵심 디자인 기준은 `BaseLayout`, 글래스/에디토리얼 패턴이다.

도구형 페이지에서 새 입력, 탭, 다운로드 버튼을 추가할 때도 기본 페이지와 충돌하지 않도록 상단 내비게이션 여백, 라이트/다크 대비, `prose` 미리보기 스타일을 확인한다.
