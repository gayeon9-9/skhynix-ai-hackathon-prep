"""작은 UTF-8 CSV를 원본 변경 없이 읽는 공통 함수. Python 3.10+ 표준라이브러리만 사용."""

import csv
import json
import sys
from pathlib import Path


def read_csv(path):
    """헤더와 행 길이를 검증한다. 값과 키는 원문 문자열 그대로 보존한다."""
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle, strict=True)
        header = next(reader, None)
        if not header or any(not name.strip() for name in header):
            raise ValueError(f"{path}: 비어 있는 파일 또는 빈 열 이름입니다.")
        if len(header) != len(set(header)):
            raise ValueError(f"{path}: 중복된 열 이름이 있습니다.")
        rows = []
        for record_no, cells in enumerate(reader, start=2):
            if len(cells) != len(header):
                raise ValueError(
                    f"{path}: {record_no}번째 CSV 레코드의 열 수가 "
                    f"{len(cells)}개입니다. 헤더는 {len(header)}개입니다."
                )
            rows.append(dict(zip(header, cells)))
    return header, rows


def write_json(result):
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))


def report_error(error):
    print(f"오류: {error}", file=sys.stderr)
    return 2


INPUT_ERRORS = (OSError, UnicodeError, csv.Error, ValueError)
