# Design Principles

## Extend From The Archive Tone

DevArchive는 제품 랜딩 페이지보다 개인 개발 아카이브에 가깝다. 화면은 설명을 과하게 늘어놓기보다 제목, 기록, 목록, 본문을 명확하게 보여준다.

새 요소를 만들 때는 이 톤을 고정된 규칙으로 묶기보다, 기존 화면에서 반복된 스타일을 출발점으로 삼아 자연스럽게 확장한다.

## Editorial First

큰 제목은 `Playfair Display` 기반 세리프와 강한 무게감으로 페이지의 인상을 만든다. 본문과 UI 조작 요소는 `Inter` 기반 산세리프로 정리한다.

## High Contrast With Restrained Accent

기본 색은 흰색/검정 또는 다크 배경/크림 텍스트다. 강조는 레드 계열 `--accent-color`를 우선 사용한다. 아티클 필터처럼 상태 표시가 필요한 곳은 기존 블루 계열을 참고한다. 새 색상이 필요하면 기존 변수와 조화를 이루는지 먼저 확인한다.

## Glass As Container

주요 카드와 내비게이션은 반투명 배경, blur, 얇은 보더, 내부 하이라이트를 사용한다. 글래스 효과는 장식이 아니라 콘텐츠 그룹을 구분하는 컨테이너 역할이다.

## Motion Is Slow And Minimal

진입 애니메이션은 `reveal-up`처럼 opacity와 translate 중심의 흐름을 우선 참고한다. hover는 scale, color, opacity, arrow rotation 같은 기존 반응과 비슷한 밀도에서 확장한다.

## Static Structure First

이 프로젝트는 정적 HTML/CSS/Astro 기반 사이트다. 디자인 일관성을 위해 현재 구조를 기본값으로 삼고, 큰 구조 변경이나 UI 라이브러리 도입은 명확한 필요가 있을 때만 검토한다.
