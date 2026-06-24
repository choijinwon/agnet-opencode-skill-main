# Start Guide

새 채팅 세션의 첫 assistant 응답에서는 사용자의 첫 입력 내용과 관계없이 Launch Guide를 먼저 출력합니다.

적용 예:

- `하이`
- `안녕`
- `아무거나`
- `분석해줘`
- `sklearn 샘플 생성해줘`
- 그 밖의 구체적인 작업 요청

Launch Guide를 먼저 출력한 뒤에는 다음 기준으로 이어서 응답합니다.

- 첫 메시지가 구체적인 요청이면 바로 그 요청을 계속 처리합니다.
- 첫 메시지가 인사나 모호한 메시지뿐이면 무엇을 먼저 확인할지 묻습니다.
- 같은 채팅 세션에서는 사용자가 명시적으로 다시 요청하지 않는 한 Launch Guide를 반복 출력하지 않습니다.

다음 표현은 Launch Guide 재출력 요청으로 처리합니다.

- `/launch`
- `런치 가이드`
- `처음 안내 다시`
- `시작 가이드`
- `launch guide`

보안 규칙:

- API keys, passwords, tokens, secret values를 출력하지 않습니다.
- secret-like field는 `set`, `empty`, `missing` 상태만 말합니다.
