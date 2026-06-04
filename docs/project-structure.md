# Project Structure

## Root

- `README.md`: 프로젝트 문서 인덱스
- `AGENTS.md`: AI 에이전트 작업 규칙
- `docs/`: 상세 문서
- `astro.config.mjs`: Astro 설정
- `package.json`: 스크립트와 의존성
- `public/`: 정적 파일, favicon, 영상, 클라이언트 스크립트
- `src/`: 페이지, 레이아웃, 컴포넌트, 스타일, 콘텐츠
- `dist/`: 빌드 결과물

## Source Tree

- `src/pages/`: 라우트 단위 Astro 페이지
- `src/pages/articles/`: 아티클 목록과 상세 라우트
- `src/pages/project/`: 프로젝트 상세 라우트
- `src/components/`: 내비게이션, 푸터, 카드, 토픽 사이드바 등 재사용 컴포넌트
- `src/layouts/`: 공통 HTML 구조와 전역 스타일 로딩
- `src/styles/global.css`: Tailwind 설정, 디자인 토큰, 공통 컴포넌트 스타일
- `src/content/articles/`: Markdown 아티클 콘텐츠
- `src/assets/`: 로고와 이미지 자산

## Layouts

`src/layouts/BaseLayout.astro`가 현재 사이트의 기본 레이아웃이다. Google Fonts, Material Symbols, 전역 CSS, 테마 적용 스크립트, `Navbar`, `Footer`를 포함한다.

`src/layouts/Layout.astro`는 Astro 기본 템플릿에 가까운 레이아웃이며, 현재 주요 페이지의 디자인 기준은 아니다. 새 페이지는 특별한 이유가 없으면 `BaseLayout.astro`를 사용한다.

## Pages

- `/`: 큰 에디토리얼 히어로와 Articles/Works 목록
- `/articles`: 아티클 피드/그리드 목록, 카테고리 필터, 토픽 사이드바
- `/articles/[slug]`: 아티클 상세, 본문 카드, 좌측 토픽, 우측 목차
- `/project`: 프로젝트 카드 목록
- `/project/[slug]`: 프로젝트 상세 기록
- `/about`: 소개, 이력, 기술 스택, 자격 정보
- `/write`, `/write-project`, `/snippets`: 작성/보조/실험 성격의 정적 도구 페이지

## Content

아티클은 `src/content/articles/` 아래 Markdown 파일로 관리한다. 이미지는 아티클 하위 `images/` 폴더에 둔다.
