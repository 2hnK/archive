# Page Patterns

## Home

- 큰 세리프 히어로 문장
- accent line으로 시각적 리듬 형성
- 짧은 소개 문장은 우측 정렬과 좌측 border로 보조
- 하단은 Articles/Works 2열 editorial list

## Articles Index

- 상단에 큰 `Articles` 제목과 작은 subtitle
- feed/grid view toggle
- `xl` 이상: 좌측 토픽 사이드바, 중앙 900px 콘텐츠
- `xl` 미만: 모바일 category chip
- feed view는 큰 `glass-panel` 카드
- grid view는 `ArticleCard` 2열

## Article Detail

- 상단 title/meta bar
- 3열 구조: 좌측 topic, 중앙 article card, 우측 TOC
- 본문은 `glass-panel` 안의 `.prose`
- 목차는 sliding highlight와 scroll spy

## Project Index

- 큰 `Works` 제목
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

- 중앙 hero와 짧은 인용문
- 은은한 accent glow
- 중앙선 타임라인
- glass card milestone
- 1px hairline 기술 그리드
- border-bottom 기반 인증 리스트

## Tool Pages

`/write`, `/write-project`, `/snippets`는 보조 도구 성격이 강하다. 일부 zinc 계열, rounded input, form UI가 사용되지만, 공개 아카이브 페이지의 핵심 디자인 기준은 `BaseLayout`, 글래스/에디토리얼 패턴이다.
