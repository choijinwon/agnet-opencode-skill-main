# OpenCode MLflow Skills

이 폴더는 ML 전문가와 주니어가 같은 흐름으로 MLflow 모델 프로젝트를 점검할 수 있게 돕는 OpenCode skill 모음입니다.

## Workflow

```text
1. Project Analyze
   model_found: true | false 결정

2. Sample Bootstrap
   모델이 없으면 1 sklearn / 2 pytorch / 3 tensorflow 선택

3. Environment Check
   Python 3.11.9, dependency, MLflow, 설정 상태 확인

4. Train Model
   실제 entrypoint로 로컬 학습/모델 생성 실행

5. Inference Test
   input_example 기반 predict contract와 schema 확인

6. MLflow Verify
   run, metrics, artifact, registry 상태 확인
```

## Common UI Pattern

각 스킬은 `판단 결과`를 먼저 보여주고, 자세한 설명은 접기 영역에 둡니다.

```text
Result First
Workflow
What To Do Now
Output Contract
Commands
Artifact Map
details: 자세한 판단 기준
details: 문제 해결
details: 전문가 상세
details: Safety 규칙
```

## Status Meaning

```text
pass:
  정상 또는 다음 단계 진행 가능

warn:
  진행 가능하지만 호환성/권한/환경 확인 필요

needs_user_input:
  사용자가 값, 파일명, 샘플 선택, 덮어쓰기 여부를 결정해야 함

blocked:
  현재 단계 진행 불가. 원인 해결 필요
```

## Artifact Map

```text
local metrics   -> ai_studio/metrics/
local code      -> ai_studio/code/
MLflow artifact -> artifact_path="ai_studio" 아래 code/
tracking store  -> ai_studio/tracking/
```

## Shared Safety

- Launch 모드는 읽기 전용입니다.
- Build 모드에서만 파일 복사, 수정, 설치, 실행을 수행합니다.
- secret 값은 출력하지 않고 `set`, `empty`, `missing` 상태만 표시합니다.
- Bun은 사용하지 않습니다.
- JavaScript 패키지 설치가 필요하고 `package.json`이 있으면 `npm i`만 사용합니다.
- 폐쇄망 WSL에서는 `.opencode/wsl/install_offline.sh`를 우선 사용합니다.
- Windows에서는 `standaloneExecutable` 또는 native executable 흐름보다 Python script 흐름을 우선합니다.
