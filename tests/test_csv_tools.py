"""CLI 입출력과 잘못된 데이터가 조용히 누락되지 않는지 확인한다."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CsvToolsTest(unittest.TestCase):
    def run_tool(self, name, *args):
        return subprocess.run([sys.executable, str(ROOT / "snippets" / name), *map(str, args)],
                              text=True, capture_output=True, check=False)

    def make_csv(self, directory, name, text, bom=False):
        path = Path(directory) / name
        path.write_text(text, encoding="utf-8-sig" if bom else "utf-8")
        return path

    def test_example_differences_and_inputs_unchanged(self):
        before = ROOT / "examples/inspection_before.csv"
        after = ROOT / "examples/inspection_after.csv"
        snapshots = [p.read_bytes() for p in (before, after)]
        result = self.run_tool("compare_csv.py", before, after, "--key", "inspection_id")
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["only_left"][0]["key"], {"inspection_id": "0004"})
        self.assertEqual(report["only_right"][0]["key"], {"inspection_id": "0006"})
        self.assertEqual([r["key"]["inspection_id"] for r in report["changed_rows"]], ["0002", "0003"])
        self.assertEqual([p.read_bytes() for p in (before, after)], snapshots)

    def test_profile_missing_duplicate_and_nonfinite(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.make_csv(tmp, "data.csv", "id,value\n001,2\n001,2\n002,NA\n003,inf\n", bom=True)
            snapshot = path.read_bytes()
            result = self.run_tool("profile_csv.py", path)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout, parse_constant=lambda x: self.fail(f"비표준 JSON: {x}"))
            self.assertEqual(report["duplicate_row_count"], 1)
            col = report["column_profiles"]["value"]
            self.assertEqual(col["missing_candidate_count"], 1)
            self.assertEqual(col["non_finite_numeric_count"], 1)
            self.assertIsNone(col["numeric_summary_candidate"])
            self.assertEqual(report["column_profiles"]["id"]["sample_raw_values"][0], "001")
            self.assertEqual(path.read_bytes(), snapshot)

    def test_identical_with_reordered_columns_bom_and_composite_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            left = self.make_csv(tmp, "a.csv", "id,part,value\n001,A,10\n001,B,20\n")
            right = self.make_csv(tmp, "b.csv", "value,part,id\n20,B,001\n10,A,001\n", bom=True)
            result = self.run_tool("compare_csv.py", left, right, "--key", "id", "part")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(json.loads(result.stdout)["identical"])

    def test_leading_zero_is_not_removed(self):
        with tempfile.TemporaryDirectory() as tmp:
            left = self.make_csv(tmp, "a.csv", "id,value\n001,10\n")
            right = self.make_csv(tmp, "b.csv", "id,value\n1,10\n")
            result = self.run_tool("compare_csv.py", left, right, "--key", "id")
            report = json.loads(result.stdout)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(report["only_left"][0]["key"]["id"], "001")
            self.assertEqual(report["only_right"][0]["key"]["id"], "1")

    def test_invalid_tables_are_rejected(self):
        cases = {
            "duplicate_key": "id,value\n001,10\n001,20\n",
            "blank_key": "id,value\n ,10\n",
            "duplicate_header": "id,id\n001,10\n",
            "empty_header": "id,\n001,10\n",
            "extra_cell": "id,value\n001,10,20\n",
            "short_row": "id,value\n001\n",
            "different_columns": "id,other\n001,10\n",
        }
        with tempfile.TemporaryDirectory() as tmp:
            good = self.make_csv(tmp, "good.csv", "id,value\n001,10\n")
            for label, content in cases.items():
                with self.subTest(case=label):
                    bad = self.make_csv(tmp, "bad.csv", content)
                    result = self.run_tool("compare_csv.py", good, bad, "--key", "id")
                    self.assertEqual(result.returncode, 2, result.stdout)
                    self.assertIn("오류:", result.stderr)
                    self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
