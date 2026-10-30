# AI 문제 해결 준비 자료

반도체 기초를 이해하고, 데이터를 점검하고, 선택한 방법과 검증 결과를 설명하기 위한 **비공식 공개 학습 자료**입니다. 실제 시험 문제나 정답을 전제로 하지 않습니다.

**먼저 볼 문서:** [활용 순서](guides/START_HERE.md) → [반도체 기초](domain/semiconductor_basics.md) → [공식 자료와 출처](references/SOURCES.md)

## 무엇이 들어 있나요?

| 자료 | 용도 |
| --- | --- |
| [반도체 기초 요약](domain/semiconductor_basics.md) | 제품·공정·검사 용어와 업무에서 확인할 질문 |
| [공식 자료 목록](references/SOURCES.md) | 기업 공식 설명, 공개 연습 데이터, 데이터 처리·검증 문서 |
| [CSV 상태 확인](snippets/profile_csv.py) | 행·열, 결측, 중복, 값의 분포를 확인 |
| [두 CSV 대조](snippets/compare_csv.py) | 식별키를 기준으로 누락·추가·변경을 확인 |
| [합성 예제와 실행 안내](examples/README.md) | 도구 실행 방법과 결과를 해석하는 작은 연습 |
| [작업 계획 양식](templates/task_plan.md) | 목표, 입력·출력, 제약, 성공 기준을 정리 |
| [판단 기록 양식](templates/decision_log.md) | 선택 이유, 확인한 사실, 검증 결과, 한계를 기록 |
| [검증 기록 양식](templates/verification.md) | 정상·누락·중복·경계 상황을 확인 |
| [자기 설명 연습](guides/SELF_REVIEW.md) | 사용한 방법과 수정 내용을 본인의 말로 설명 |

## 5분 안에 실행하기

Python **3.10 이상**과 표준 라이브러리만 사용합니다. 별도 패키지 설치나 외부 API 키가 필요하지 않습니다.

```bash
git clone --depth 1 https://github.com/gayeon9-9/skhynix-ai-hackathon-prep.git
cd skhynix-ai-hackathon-prep
python3 snippets/profile_csv.py examples/inspection_before.csv
python3 snippets/compare_csv.py examples/inspection_before.csv examples/inspection_after.csv --key inspection_id
```

대조 예제는 일부 값을 의도적으로 바꾸었으므로 **차이가 발견되는 것이 정상**입니다. 대조 도구는 일치 `0`, 차이 발견 `1`, 입력·실행 오류 `2`를 종료 코드로 사용합니다. 출력 내용과 함께 판단하세요.

기능 확인:

```bash
python3 -m unittest discover -s tests -v
```

## 실제 과제에 적용하는 순서

1. 제공된 README와 과제 조건을 먼저 읽습니다. 필수 파일명·제출 위치·데이터 정의를 확인합니다.
2. 필요한 경우 이 저장소를 별도 참고 폴더로 가져옵니다. 제공 프로젝트를 덮어쓰지 않습니다.
3. 자료 목록에서 현재 작업과 관련 있는 문서·코드만 확인합니다.
4. 실제 데이터의 열과 식별키에 맞게 사용하고, 작은 표본으로 결과를 확인합니다.
5. 활용한 자료, 직접 바꾼 부분, 검증 결과와 남은 한계를 기록합니다.

이 저장소는 별도의 에이전트 실행 환경이나 자동 설치 도구가 아닙니다. 문서와 소형 Python 도구를 필요한 범위에서 읽고 실행하는 구성입니다. 제공 환경의 지침과 해당 과제 규칙이 우선입니다. 허용된 참고 자료 활용 여부는 응시자가 실제 안내를 기준으로 확인해야 합니다.

## 데이터와 해석의 범위

- `examples/`는 직접 만든 작은 합성 데이터입니다. 실제 기업·반도체 제조 데이터 또는 시험 제공 데이터가 아닙니다.
- 원본 CSV를 수정하거나 결측·이상치를 자동 제거하지 않습니다.
- 대조는 지정한 식별키와 값의 차이를 확인하는 작업입니다. 차이의 업무상 의미는 별도 판단이 필요합니다.
- 공개 데이터 원본, 기업 기사·그림, 외부 라이브러리 전체 소스는 포함하지 않습니다. 필요한 자료의 원문 링크와 이용 조건은 출처 문서에서 확인합니다.
- 실제 과제의 입력·기록·결과는 해당 과제의 허용된 작업 공간에서만 다룹니다.

## 이용 조건

이 저장소에서 직접 작성한 코드·문서·합성 예제는 [MIT License](LICENSE)를 적용합니다. 연결된 외부 자료에는 각 원저작자의 별도 이용 조건이 적용됩니다. [출처와 재사용 안내](references/SOURCES.md)를 확인하세요.

작성 기준일: **2026-10-30**. 기본 개념을 정리한 자료이며 최신 제품 성능·시장 점유율·출제 정보를 제공하지 않습니다.
