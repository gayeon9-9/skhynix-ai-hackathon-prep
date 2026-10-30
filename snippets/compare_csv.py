#!/usr/bin/env python3
"""두 작은 CSV를 키로 대조한다. 일치=0, 차이 발견=1, 입력 오류=2."""

import argparse

from _csv_tools import INPUT_ERRORS, read_csv, report_error, write_json


def index_rows(rows, keys, label):
    indexed = {}
    for record_no, row in enumerate(rows, start=2):
        key = tuple(row[name] for name in keys)
        if any(not item.strip() for item in key):
            raise ValueError(f"{label}: {record_no}번째 CSV 레코드에 빈 키가 있습니다.")
        if key in indexed:
            raise ValueError(f"{label}: 중복 키 {key!r}가 있습니다. 비교를 중단합니다.")
        indexed[key] = row
    return indexed


def compare(left_path, right_path, keys):
    left_header, left_rows = read_csv(left_path)
    right_header, right_rows = read_csv(right_path)
    if len(keys) != len(set(keys)):
        raise ValueError("--key에 같은 열을 두 번 지정했습니다.")
    if set(left_header) != set(right_header):
        raise ValueError("두 CSV의 열 이름 구성이 다릅니다. 열 매핑을 먼저 확인하세요.")
    missing = [name for name in keys if name not in left_header]
    if missing:
        raise ValueError(f"키 열을 찾을 수 없습니다: {missing}")
    left = index_rows(left_rows, keys, str(left_path))
    right = index_rows(right_rows, keys, str(right_path))

    def entry(key, row):
        return {"key": dict(zip(keys, key)), "row": row}

    changed = []
    for key in left:
        if key in right:
            cells = {name: {"left": left[key][name], "right": right[key][name]}
                     for name in left_header if left[key][name] != right[key][name]}
            if cells:
                changed.append({"key": dict(zip(keys, key)), "cells": cells})
    only_left = [entry(key, row) for key, row in left.items() if key not in right]
    only_right = [entry(key, row) for key, row in right.items() if key not in left]
    result = {
        "comparison": "원문 문자열 비교: 공백·숫자 표기 차이도 차이로 취급",
        "key_columns": keys,
        "left_row_count": len(left_rows), "right_row_count": len(right_rows),
        "only_left": only_left, "only_right": only_right, "changed_rows": changed,
        "identical": not (only_left or only_right or changed),
    }
    return result


def main():
    parser = argparse.ArgumentParser(description="CSV를 키로 비교합니다. 종료 코드: 일치 0 / 차이 1 / 오류 2")
    parser.add_argument("left", help="기준 CSV")
    parser.add_argument("right", help="비교 CSV")
    parser.add_argument("--key", nargs="+", required=True, help="식별키 열 이름. 복합키는 여러 개 지정")
    args = parser.parse_args()
    try:
        result = compare(args.left, args.right, args.key)
        write_json(result)
        return 0 if result["identical"] else 1
    except INPUT_ERRORS as error:
        return report_error(error)


if __name__ == "__main__":
    raise SystemExit(main())
