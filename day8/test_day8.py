import unittest
from day8 import part1, line_of_sight, count_visible

DATA = """
30373
25512
65332
33549
35390
"""


class TestSuite(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1(""), None)

    def test_line_of_sight(self):
        expected = [
            "30373",
            "25512",
            "65332",
            "33549",
            "35390",
            "32633",
            "05535",
            "35353",
            "71349",
            "32290",
        ]
        self.assertCountEqual(line_of_sight(DATA), expected)

    def test_count_visible(self):
        self.assertEqual(count_visible("30373"), 1)


if __name__ == "__main__":
    unittest.main()
