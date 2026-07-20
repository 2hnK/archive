---
type: Design Reference
title: Typography
description: DevArchive의 폰트 패밀리, 제목, 본문, 메타 라벨, 코드 타이포그래피 기준.
tags: ["design", "typography", "tokens"]
timestamp: "2026-07-21T00:00:00+09:00"
---

# Typography

## Font Families

`src/styles/global.css`의 테마 변수 기준:

- Serif: `"Newsreader", "Noto Serif KR", serif`
- Sans: `"Manrope", "Noto Sans KR", sans-serif`
- Mono: `"IBM Plex Mono", "Noto Sans KR", monospace`

영문과 한글이 섞인 제목에서는 각 계열의 한글 fallback을 함께 사용해 획의 대비와 본문 밀도가 자연스럽게 이어지도록 한다.

한글 세리프에는 `Noto Serif KR`, 한글 본문과 UI에는 `Noto Sans KR`을 사용한다. 두 글꼴의 중립적인 획과 폭을 활용해 한글·영문 혼용 제목과 긴 기술 설명의 안정적인 리듬을 유지한다. 두 글꼴은 SIL Open Font License를 따르며, 배포 조건은 [Noto Fonts](https://github.com/notofonts/noto-fonts)의 공식 저장소를 기준으로 한다.

## Headings

전역 `h1`-`h6`는 세리프, `font-weight: 700`, `line-height: 1.1`, `letter-spacing: -0.02em`을 기본으로 한다.

페이지 히어로는 `font-black`, `tracking-tighter`, `uppercase`, 큰 viewport 기반 크기를 자주 사용한다. 단, 작은 패널 내부에는 hero급 크기를 사용하지 않는다.

About 인사말은 프로필과 함께 있는 제한된 패널 안에서 한 줄을 우선하고 `clamp` 기반 크기로 조절한다. sticky rail의 섹션 제목은 rail 폭을 넘지 않도록 긴 제목에 별도 크기 변형을 허용한다.

## Body

본문은 산세리프 중심이며, Markdown 본문은 `.prose`가 담당한다.

- 기본 크기: `1rem` 또는 페이지별 `17px`
- line-height: `1.7`-`1.8`
- opacity: `0.7`-`0.9` 범위로 보조 텍스트 위계를 만든다.

## Metadata And Labels

메타 정보, 카테고리, 버튼 라벨은 다음 특징을 따른다.

- `text-[8px]`-`text-[13px]`
- uppercase
- `tracking-widest` 또는 `tracking-[0.2em]` 이상
- `font-bold`
- 낮은 opacity

## Code

인라인 코드는 `--accent-color`와 옅은 배경을 사용한다. 코드 블록은 텍스트/배경 반전 구조와 mono font를 유지한다.

도구형 페이지의 에디터/미리보기 영역은 mono font와 `.prose` 규칙을 함께 사용하되, 공개 아카이브 본문보다 더 조밀한 UI 라벨을 허용한다.
