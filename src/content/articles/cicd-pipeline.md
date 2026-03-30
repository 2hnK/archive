---
title: "CI/CD 파이프라인 우아하게 구축하기"
description: "GitHub Actions와 Docker를 활용한 브랜치별 무중단 배포 전략"
category: "DevOps"
subcategory: "CI/CD"
date: 2026-03-28
tags: ["GitHub Actions", "Docker", "Deployment"]
---
팀에 새로운 멤버가 합류했을 때, 배포 과정을 따로 설명해야 한다면 그 자체로 기술 부채입니다. 개발자는 오직 코드에만 집중하고 머지(Merge) 버튼을 누르면 모든 테스트와 배포가 자동으로 흘러가야 합니다.

## GitHub Actions의 강력함
단 몇 줄의 YAML 스크립트만으로 커스텀 워크플로우를 구성할 수 있다는 것은 엄청난 매력입니다. 이번 포스트에서는 main 브랜치와 dev 브랜치를 분리하고, 도커 빌드 후 AWS 서버에 무중단(Blue/Green)으로 배포하는 파이프라인을 처음부터 바닥까지 구축하는 과정을 공유합니다.
