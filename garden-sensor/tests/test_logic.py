import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "firmware"))
import logic  # noqa: E402


class RawToPercent(unittest.TestCase):
    def test_dry_is_zero_and_wet_is_hundred(self):
        self.assertEqual(logic.raw_to_percent(50000, 50000, 25000), 0.0)
        self.assertEqual(logic.raw_to_percent(25000, 50000, 25000), 100.0)

    def test_halfway(self):
        self.assertAlmostEqual(logic.raw_to_percent(37500, 50000, 25000), 50.0)

    def test_clamps_outside_the_range(self):
        self.assertEqual(logic.raw_to_percent(60000, 50000, 25000), 0.0)
        self.assertEqual(logic.raw_to_percent(10000, 50000, 25000), 100.0)

    def test_works_when_wet_reads_higher_than_dry(self):
        self.assertAlmostEqual(logic.raw_to_percent(30000, 20000, 40000), 50.0)

    def test_same_calibration_values_is_an_error(self):
        with self.assertRaises(ValueError):
            logic.raw_to_percent(1000, 5000, 5000)


class CsvRow(unittest.TestCase):
    def test_normal_row(self):
        self.assertEqual(logic.csv_row(600, 41000, 36.04, 21.46, 55.0), "600,41000,36.0,21.5,55.0")

    def test_missing_air_reading_leaves_empty_cells(self):
        self.assertEqual(logic.csv_row(1200, 41000, 36.0, None, None), "1200,41000,36.0,,")

    def test_header_matches_row_width(self):
        row = logic.csv_row(1, 2, 3.0, 4.0, 5.0)
        self.assertEqual(len(logic.CSV_HEADER.split(",")), len(row.split(",")))


if __name__ == "__main__":
    unittest.main()
