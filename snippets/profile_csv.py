#!/usr/bin/env python3
"""작은 CSV의 상태를 확인한다. 삭제·대체·형변환을 원본에 적용하지 않는다."""

import argparse
import math
from collections import Counter

from _csv_tools import INPUT_ERRORS, read_csv, report_error, write_json


MISSING_CANDIDATES = {"", "na", "n/a", "null", "none", "nan"}


def describe_column(values):
    # 결측 표시는 후보 규칙일 뿐이다. 'NA'가 실제 코드인지는 사람이 판단한다.
    observed = [v for v in values if v.strip().lower() not in MISSING_CANDIDATES]
    counts = Counter(observed)
    numbers, non_finite = [], 0
    for value in observed:
        try:
            number = float(value)
        except ValueError:
            continue
        if math.isfinite(number):
            numbers.append(number)
        else:
            non_finite += 1
    summary = None
    # 모든 관측값이 유한한 수로 읽힐 때만 계산한다. 식별번호도 후보가 될 수 있다.
    if observed and len(numbers) == len(observed):
        summary = {
            "min": min(numbers), "max": max(numbers),
            "mean": math.fsum(v / len(numbers) for v in numbers),
        }
    return {
        "missing_candidate_count": len(values) - len(observed),
        "distinct_non_missing_count": len(counts),
        "repeated_non_missing_value_count": len(observed) - len(counts),
        "sample_raw_values": list(dict.fromkeys(values))[:5],
        "finite_numeric_count": len(numbers),
        "non_finite_numeric_count": non_finite,
        "numeric_summary_candidate": summary,
    }


def main():
    parser = argparse.ArgumentParser(description="CSV 상태를 읽기만 하고 JSON으로 출력합니다.")
    parser.add_argument("csv_path", help="작은 UTF-8 또는 UTF-8 BOM CSV 파일")
    args = parser.parse_args()
    try:
        header, rows = read_csv(args.csv_path)
        write_json({
            "row_count": len(rows), "column_count": len(header), "columns": header,
            "duplicate_row_count": len(rows) - len({tuple(r.values()) for r in rows}),
            "missing_candidate_tokens": sorted(MISSING_CANDIDATES),
            "column_profiles": {name: describe_column([r[name] for r in rows]) for name in header},
            "notes": [
                "모든 값은 CSV 문자열이며 원본을 변경하지 않았습니다.",
                "결측·숫자 판정은 후보입니다. 식별번호, 단위, 업무 의미를 확인하세요.",
                "숫자 요약은 부동소수점 근사값입니다. 금액 정산의 정확한 계산용이 아닙니다.",
            ],
        })
        return 0
    except INPUT_ERRORS as error:
        return report_error(error)


if __name__ == "__main__":
    raise SystemExit(main())
