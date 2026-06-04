# Typography

## Font Families

`src/styles/global.css`의 테마 변수 기준:

- Serif: `"Playfair Display", serif`
- Sans: `"Inter", sans-serif`
- Mono: `"Fira Code", "JetBrains Mono", monospace`

## Headings

전역 `h1`-`h6`는 세리프, `font-weight: 700`, `line-height: 1.1`, `letter-spacing: -0.02em`을 기본으로 한다.

페이지 히어로는 `font-black`, `tracking-tighter`, `uppercase`, 큰 viewport 기반 크기를 자주 사용한다. 단, 작은 패널 내부에는 hero급 크기를 사용하지 않는다.

## Body

본문은 산세리프 중심이며, Markdown 본문은 `.prose`가 담당한다.

- 기본 크기: `1rem` 또는 페이지별 `17px`
- line-height: `1.7`-`1.8`
- opacity: `0.7`-`0.9` 범위로 보조 텍스트 위계를 만든다.

## Metadata And Labels

메타 정보, 카테고리, 버튼 라벨은 다음 특징을 따른다.

- `text-[10px]`-`text-[13px]`
- uppercase
- `tracking-widest` 또는 `tracking-[0.2em]` 이상
- `font-bold`
- 낮은 opacity

## Code

인라인 코드는 `--accent-color`와 옅은 배경을 사용한다. 코드 블록은 텍스트/배경 반전 구조와 mono font를 유지한다.
