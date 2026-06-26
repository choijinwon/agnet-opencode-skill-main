# Launch Guide

```text
OpenCode MLflow Launch

1. 먼저 분석
   어떤 단어로 시작해도 현재 워크스페이스를 먼저 확인합니다.
   확인 결과는 model_found: true 또는 model_found: false로 알려줍니다.

2. 모델이 있으면
   사용자 모델 경로를 기준으로 진행합니다.
   모델 파일은 프로젝트 루트의 data/ 하위 원본 경로에서 직접 읽습니다.
   모델 파일을 ai_studio/로 복사하지 않습니다.
   ai_studio/는 실행 템플릿과 산출물 폴더로만 사용합니다.
   기존 runtest.py는 수정하지 않고 runtest_2.py를 생성해 테스트합니다.

   진행 순서
   1. data/** 모델 목록 확인
   2. 사용할 모델 선택
   3. 선택 모델 위치 확인
   4. 모델 형식 판별
   5. ai_studio 템플릿 폴더 준비
   6. 선택 모델 직접 읽기
   7. runtest.py 참조
   8. runtest_2.py 생성
   9. 환경 검증
   10. 추론 테스트
   11. MLflow 검증

3. 모델이 없으면
   Build 모드에서 샘플을 선택합니다.

   1 -> sklearn
   2 -> pytorch
   3 -> tensorflow

   샘플은 루트에 파일을 흩뿌리지 않고 아래처럼 폴더째 복사합니다.
   <workspace>/sklearn_sample/
   <workspace>/pytorch_sample/
   <workspace>/tensorflow_sample/

4. Launch 모드 규칙
   Launch 모드는 읽기 전용입니다.
   파일 생성, 수정, 삭제, 복사, 설치, 모델 실행은 Build 모드에서만 합니다.

5. 폐쇄망/Windows 기준
   - Bun 사용 금지: bun, bunx, bun install, bun run
   - JavaScript 설치가 필요하고 package.json이 있으면 npm i 사용
   - WSL wheelhouse가 있으면 bash .opencode/wsl/install_offline.sh 우선
   - 응답/인덱싱이 느리면 python .opencode/scripts/response_speed_check.py --project . 실행
   - 진단 후 python .opencode/scripts/apply_index_ignore.py --project . 실행
   - 전체 점검은 python .opencode/scripts/doctor.py --workspace . --project . 실행
   - Windows standaloneExecutable/native 실행 대신 python 스크립트 우선

추천 첫 요청
- 이 워크스페이스를 MLflow 모델 있음/없음 기준으로 분석해줘.
- 모델이 없으면 Build 모드에서 2번 PyTorch 샘플 생성으로 진행해줘.

보안 규칙
- API key, password, token 값은 출력하지 않습니다.
- secret 값은 set, empty, missing 상태만 표시합니다.
```
