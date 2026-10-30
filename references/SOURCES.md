# 공개 참고자료와 이용 범위

확인일: **2026-10-30**. 공개된 공식 자료와 데이터 제공기관의 설명을 확인했다.
이 파일은 출처 목록이다. 아래 자료의 원문·그림·데이터·예제 코드를 저장소에 복제하지 않았다.
학습 메모는 직접 작성한 짧은 설명이며, 외부 원본에는 해당 제공자의 권리가 적용된다.
발행일을 확인하지 못한 경우 확인일로 대신 표시하지 않고 별도로 구분했다.

| ID | 자료 | 이 저장소에서의 활용 | 보관 방식 |
|---|---|---|---|
| S01 | SK하이닉스 Semiconductor 101 | DRAM·NAND·HBM 개념 | 링크와 자체 요약 |
| S02 | 삼성반도체 공정 입문자료 | 웨이퍼·다이·공정·검사 | 링크와 자체 요약 |
| S03 | UCI AI4I 2020 | 선택형 제조 데이터 연습 안내 | 링크만, 원본 미포함 |
| S04 | UCI SECOM | 선택형 반도체 데이터 연습 안내 | 링크만, 원본 미포함 |
| S05 | pandas 공식 문서 | 표 결합·대조 방법의 참고 | 링크와 자체 점검 항목 |
| S06 | scikit-learn 공식 문서 | 데이터 누수·검증 오류 방지 | 링크와 자체 점검 항목 |
| S07 | Applied Materials 용어사전 | 로트·장비·레시피 뜻 확인 | 링크와 자체 요약 |

## S01

**[Semiconductor 101] SK hynix Explains “What’s What” in the Semiconductor World** — SK hynix Newsroom

- [원문](https://news.skhynix.com/en/semiconductor-101-sk-hynix-explains-whats-what-in-the-semiconductor-world/)
- 발행일: 2024-08-14. 확인일: 2026-10-30.
- 용도: 메모리의 역할과 DRAM·NAND·HBM·TSV의 기본 뜻을 이해한다.
- 저장 방식: 짧은 한국어 자체 설명과 링크. 기사와 이미지는 포함하지 않는다.
- 이용 범위: 원문 재배포를 허용하는 오픈 라이선스는 확인하지 못했다.
- 한계: 발행 당시 제품 설명을 현재의 최신 세대·사양으로 사용하지 않는다.

## S02

**삼성반도체: 반도체 8대 공정 입문자료** — Samsung Semiconductor

- [반도체 8대 공정 한눈에 보기](https://semiconductor.samsung.com/kr/support/tools-resources/fabrication-process/semiconductor-encyclopedia-the-eight-essential-semiconductor-fabrication-processes-at-a-glance/)
- [웨이퍼와 다이](https://semiconductor.samsung.com/kr/support/tools-resources/fabrication-process/eight-essential-semiconductor-fabrication-processes-part-1-what-is-a-wafer/)
- [EDS 검사와 수율](https://semiconductor.samsung.com/kr/support/tools-resources/fabrication-process/eight-essential-semiconductor-fabrication-processes-part-8-eds-electrical-die-sorting-for-the-perfect-chips/)
- [패키징](https://semiconductor.samsung.com/kr/support/tools-resources/fabrication-process/eight-essential-semiconductor-fabrication-processes-part-9-packaging-to-protect-the-chips-from-external-elements/)
- 발행일: 확인한 페이지 본문에서 확인하지 못함. 확인일: 2026-10-30.
- 용도: 생산 단위, 제조 단계, 검사 시점과 패키징의 역할을 구분한다.
- 저장 방식: 문장과 그림을 옮기지 않고 핵심 개념을 짧게 다시 설명한다.
- 이용 범위: 원문 재배포를 허용하는 오픈 라이선스는 확인하지 못했다.
- 한계: 입문용 공정 구분이다. 실제 공정 조건·운영 기준이나 데이터 정의를 대신하지 않는다.

## S03

**AI4I 2020 Predictive Maintenance Dataset** — UCI Machine Learning Repository

- [데이터 설명·원본 제공 페이지](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset)
- [DOI: 10.24432/C5HS5C](https://doi.org/10.24432/C5HS5C)
- 기탁일: 2020-08-29. 확인일: 2026-10-30.
- 성격: 산업 설비의 예지보전을 본뜬 **합성 데이터**. 10,000행, CSV 약 510KB.
- 용도: CSV 읽기, 기초 집계, 품질 확인, 분류 검증을 연습한다.
- 이용 조건: 제공 페이지에 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)이 명시되어 있다.
- 저장 방식: 링크만 보관한다. 원본이나 샘플을 이 저장소에 포함하지 않는다.
- 추후 재배포 시: 출처·라이선스 링크를 기록하고, 가공했다면 변경 사항을 표시한다.
- 한계: 반도체 실측 자료가 아니다. ID와 여러 정답 열이 함께 있으므로 모두 입력 변수로 사용하지 않는다.
- 예: `Machine failure` 예측에 TWF·HDF·PWF·OSF·RNF 같은 고장 결과 열을 넣지 않도록 점검한다.

## S04

**SECOM** — Michael McCann, Adrian Johnston / UCI Machine Learning Repository

- [데이터 설명·원본 제공 페이지](https://archive.ics.uci.edu/dataset/179/secom)
- [DOI: 10.24432/C54305](https://doi.org/10.24432/C54305)
- 기탁일: 2008-11-18. 확인일: 2026-10-30.
- 성격: 반도체 제조 공정 자료. 1,567건 중 실패 104건이며 결측이 있다.
- 규모: 제공 페이지 기준 압축 파일 약 1.9MB, 주요 데이터 파일 약 5.1MB.
- 용도: 많은 측정 변수, 결측, 드문 실패 사례를 다루는 추가 연습.
- 이용 조건: 제공 페이지에 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)이 명시되어 있다.
- 저장 방식: 링크만 보관한다. 원본이나 샘플을 이 저장소에 포함하지 않는다.
- 추후 재배포 시: 저자·데이터명·DOI·라이선스를 표시하고 변경 여부를 기록한다.
- 한계: 최신 HBM 생산자료가 아니다. 변수 수는 실제 로딩 결과와 메타데이터를 대조한다.
- 원본의 판정 값은 `-1`이 통과, `1`이 실패다. 읽은 뒤 라벨 분포를 먼저 확인한다.

## S05

**Merge, join, concatenate and compare** — pandas 공식 문서

- [표 결합·대조 문서](https://pandas.pydata.org/docs/user_guide/merging.html)
- [공식 저장소 라이선스](https://github.com/pandas-dev/pandas/blob/main/LICENSE)
- 발행일: 배포 버전에 따라 갱신되는 문서. 확인일: 2026-10-30.
- 용도: `merge`, `compare`, 결합 키 검증(`validate`), 한쪽에만 있는 행 표시(`indicator`)를 참고한다.
- 저장 방식: 링크와 자체 점검 항목. 문서나 예제 코드를 그대로 보관하지 않는다.
- 이용 조건: 공식 저장소의 BSD 3-Clause 라이선스를 확인했다. 코드를 복제하면 관련 저작권·조건·면책 고지를 유지해야 한다.
- 한계: 결합 방법은 데이터의 실제 키 관계에 맞춰 선택한다. 실행 환경의 설치 버전도 확인한다.

## S06

**Common pitfalls and recommended practices** — scikit-learn 공식 문서

- [데이터 누수와 전처리 오류](https://scikit-learn.org/stable/common_pitfalls.html)
- [숫자·범주형 혼합 전처리 예제](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)
- [공식 저장소 라이선스](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING)
- 발행일: 배포 버전에 따라 갱신되는 문서. 확인일: 2026-10-30.
- 용도: 학습·평가 자료 분리, 학습 자료에서만 전처리 기준 학습, 예측 시점에 없는 정보의 혼입 방지.
- 저장 방식: 링크와 짧은 자체 점검 항목. 예제와 데이터를 복제하지 않는다.
- 이용 조건: BSD 3-Clause. 혼합 전처리 예제에도 해당 SPDX 식별자가 표시되어 있다. 코드 복제 시 고지를 유지한다.
- 한계: 예제의 Titanic/OpenML 다운로드나 모델 선택을 모든 과제에 그대로 적용하지 않는다.

## S07

**Technical Glossary** — Applied Materials

- [공식 용어사전](https://www.appliedmaterials.com/il/en/glossary.html)
- 발행일: 고정 발행일 확인하지 못함. 확인일: 2026-10-30.
- 확인 항목: LOT, TOOL, RECIPE. 로트와 장비, 공정 설정을 구별하는 데 사용했다.
- 저장 방식: 용어의 기본 뜻만 직접 설명하고 원문은 링크로 연결한다.
- 이용 범위: 사전 전체의 재배포를 허용하는 오픈 라이선스는 확인하지 못했다.
- 한계: 실제 로트 크기, 장비 구성, 레시피 필드는 해당 데이터 설명에서 다시 확인한다.

## 출처와 직접 만든 설명의 구분

- 개념·자료 특성은 위 출처를 연결했다. 계산 예시와 질문 목록은 학습용으로 직접 작성했다.
- 이 저장소의 라이선스가 링크된 외부 원본의 라이선스를 변경하지 않는다.
- 자료를 새로 가져올 때는 해당 파일·페이지의 현재 이용 조건과 버전을 확인한다.
