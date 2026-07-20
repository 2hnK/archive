---
type: Design Reference
title: Page Patterns
description: 홈, 아티클, 프로젝트, 소개, 도구형 페이지의 반복 레이아웃 패턴.
tags: ["design", "page-patterns", "layout"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# Page Patterns

## Home

- 개인 기술 블로그임을 먼저 알리는 작은 메타 라벨과 큰 세리프 히어로 문장
- 와이드 개인 사진은 홈의 full-bleed ambient background로 사용하고, 히어로와 다음 섹션 사이의 전환 여백까지 자연스럽게 덮는 높이로 확장
- 사진은 비교적 선명하게 노출하되 하단 단방향 gradient로 목록 진입 전에 배경색에 흡수
- 히어로 타이포그래피와 메타 라벨은 따뜻한 흰색과 깊은 shadow를 사용해 사진 위 대비를 확보
- 히어로 상단 여백과 높이는 viewport 높이 단위 대신 고정 spacing을 사용해 최근 게시물과 프로젝트의 세로 시작점을 일정하게 유지
- 배경은 desktop 기준 1280px까지 이어지고 gradient는 92% 지점부터 시작해 사진의 하단을 충분히 보여준다.
- `Archive Index` 섹션에는 중간 크기의 상단 여백을 두어 배경 이미지의 fade와 목록 사이에 과도하지 않은 호흡을 만든다.
- 별도 소개 문장과 주제 태그 없이 히어로 다음에 `Archive Index / 2026` 메타 행을 배치해 노트와 프로젝트 수를 먼저 요약한다.
- 하단은 최근 게시물과 대표 프로젝트를 약 55:45 비율로 배치한다. 노트에는 순번을, 프로젝트에는 `Selected Works` 라벨을 사용해 편집물 목록처럼 구분한다.
- Home은 React island 없이 `reveal-up`과 기존 `editorial-list` hover만 사용한다.
- 모바일에서는 두 목록을 한 열로 쌓고, 텍스트 위계와 hairline 구조를 유지한다.

## Articles Index

- 상단의 큰 `Articles` 제목과 feed/grid view toggle은 같은 row에서 하단 정렬한다.
- `xl` 이상: 좌측 토픽 사이드바와 중앙 900px 콘텐츠를 사용한다.
- `xl` 미만: 모바일 category chip을 제공한다.
- feed view는 큰 곡률의 `glass-panel` 카드, grid view는 `ArticleCard` 2열을 사용한다.
- 필터, view toggle, 현재 topic은 sliding glass highlight로 상태를 표시한다.
- 목록 하단은 필터 결과를 기준으로 계산되는 숫자형 페이지네이션 사용

## Article Detail

- 상단 title/meta bar를 사용한다.
- 좌측 topic, 중앙 article card, 우측 TOC의 3열 구조를 사용한다.
- 본문과 대표 이미지는 큰 곡률의 `glass-panel` 안에 배치한다.
- 목차는 sliding highlight와 scroll spy로 현재 위치를 표시한다.

## Project Index

- 큰 `Projects` 제목을 사용한다.
- 프로젝트마다 큰 `glass-panel` 카드를 사용한다.
- 연도 pill, 제목, 설명, 태그, 원형 arrow action을 배치한다.
- hover에서는 배경 이미지가 은은하게 드러나고 콘텐츠와 화살표가 작게 이동한다.

## Project Detail

- back link와 연도 pill, 초대형 세리프 제목을 순서대로 배치한다.
- 설명은 accent border-left로 강조한다.
- 미디어에는 큰 radius와 깊은 shadow를 적용한다.
- 하단은 sidebar meta와 prose content의 12열 구조를 사용한다.

## About

- 모바일 280px, 데스크톱 320px 너비의 3:4 프로필 사진 카드와 소개문을 나란히 배치한 editorial hero
- Hero 전체는 별도 배경 패널 없이 열어두고, 사진만 흰색 계열 테두리·중간 곡률·분리된 그림자를 가진 글래스 카드로 강조한다.
- 프로필 사진에는 오버레이·번호·메타 라벨을 두지 않는다. 이미지는 3:4 비율로 고정하고 확대하지 않으며, 카드는 기본 상태의 1도 미만 기울기에서 마우스 위치를 따라 최대 약 2도 범위로만 움직인다.
- 소개 영역은 제목, 한 문장 소개, 의도적으로 두 줄로 나눈 짧은 인용문, hairline과 소셜 링크 순서로 구성하고 인사말은 한 줄을 우선하도록 크기를 제한한다.
- 역할 나열 strip은 두지 않고, Spring 백엔드와 생성형 AI 작업 분야를 한 문장으로 설명한다.
- 이메일 복사 버튼, GitHub, Instagram은 흔들림 없이 밑줄이 확장되며 각각 사이트 accent blue, monochrome, magenta 계열 hover 색을 사용한다.
- 모바일에서는 프로필 사진과 소개문을 한 열로 쌓아 인물 구도를 유지
- 각 섹션은 220px sticky rail에 순번, kicker, 제목만 두어 간결하게 구성하며 긴 영문 제목도 rail 범위를 넘지 않게 크기를 조절한다. 순번은 현재 스크롤이 머무는 섹션만 accent blue로 표시하고 나머지는 옅은 중립색을 유지한다.
- Milestones는 원형 node 중심 timeline 대신 과정별 큰 순번과 날짜를 사용하는 Editorial Ledger로 구성한다. 성과별 하위 번호와 `Current` 라벨은 생략하고 수상 badge만 accent로 강조한다.
- Tech Specs는 하나의 큰 글래스 카드 안에 Backend, AI, Frontend, Data, Infra, Testing을 3×2 hairline 구획으로 나눈 directory로 구성한다. 각 구획은 20px 상하·24px 좌우 패딩을 사용하고 기술 목록의 하단선을 같은 높이로 맞춘다. 기술 표식은 Simple Icons 기반 SVG를 같은 규격으로 렌더링하고 항상 각 브랜드 원색을 표시하며, 구획 hover에는 미세한 크기 변화만 사용한다. 공식 표식이 없는 항목은 가장 가까운 플랫폼 아이콘을 사용한다.
- Certifications는 번호·취득일, 자격명·발급처, 우측 상단 원본 색상 로고와 하단 verified 상태를 구분한 2열 credential register로 구성한다. Milestones와 함께 통합 글래스 카드의 외곽 상·하단선은 생략하고 내부 구분선만 유지한다.
- Milestone, Tech Specs, Certifications의 hover는 accent hairline/텍스트, 아주 작은 이동, 옅은 단방향 배경을 공통 규칙으로 사용한다.

## Global Footer

- 페이지 콘텐츠와 분리되는 상단 hairline을 가진 화면 폭 전체의 낮은 글래스 밴드다.
- 내부는 `max-w-[1700px]`로 제한하고 브랜드, Navigation, Contact를 데스크톱 한 행에 배치한다.
- `Archive footer / 연도` 메타와 짧은 파란 선으로 About의 에디토리얼 문법을 연결한다.
- 하단에는 저작권·지역과 `Back to top`만 두며 큰 곡률, 넓은 여백, 전체 패널 hover는 사용하지 않는다.

## Tool Pages

`/write`, `/write-project`, `/snippets`는 보조 도구 성격이 강하다. 일부 zinc 계열, rounded input, form UI가 사용되지만, 공개 아카이브 페이지의 핵심 디자인 기준은 `BaseLayout`, 글래스/에디토리얼 패턴이다.

도구형 페이지에서 새 입력, 탭, 다운로드 버튼을 추가할 때도 기본 페이지와 충돌하지 않도록 상단 내비게이션 여백, 라이트/다크 대비, `prose` 미리보기 스타일을 확인한다.
