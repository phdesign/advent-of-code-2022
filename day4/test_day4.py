import unittest
import day4


class TestDay4(unittest.TestCase):
    def test_range_contains(self):
        self.assertFalse(day4.range_contains("2-4", "6-8"))
        self.assertTrue(day4.range_contains("2-8", "3-7"))


if __name__ == "__main__":
    unittest.main()
