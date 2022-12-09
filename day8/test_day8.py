import unittest
from day8 import part1

DATA = """
30373
25512
65332
33549
35390
"""


class TestSuite(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1(DATA), 21)


if __name__ == "__main__":
    unittest.main()
