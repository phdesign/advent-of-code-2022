import unittest
import day4


class TestDay4(unittest.TestCase):
    def test_range_contains(self):
        self.assertFalse(day4.range_contains("2-4", "6-8"))
        self.assertFalse(day4.range_contains("5-7", "7-9"))
        self.assertTrue(day4.range_contains("2-8", "3-7"))
        self.assertTrue(day4.range_contains("6-6", "4-6"))
        self.assertTrue(day4.range_contains("59-59", "49-73"))
        self.assertTrue(day4.range_contains("49-73", "59-59"))
        self.assertTrue(day4.range_contains("1-1", "1-1"))

    def test_range_overlaps(self):
        self.assertFalse(day4.range_overlaps("2-4", "6-8"))
        self.assertFalse(day4.range_overlaps("8-8", "2-2"))
        self.assertTrue(day4.range_overlaps("5-7", "7-9"))
        self.assertTrue(day4.range_overlaps("7-9", "5-7"))
        self.assertTrue(day4.range_overlaps("2-8", "3-7"))
        self.assertTrue(day4.range_overlaps("6-6", "4-6"))
        self.assertTrue(day4.range_overlaps("59-59", "49-73"))
        self.assertTrue(day4.range_overlaps("49-73", "59-59"))
        self.assertTrue(day4.range_overlaps("1-1", "1-1"))
        self.assertTrue(day4.range_overlaps("1-3", "2-4"))
        self.assertTrue(day4.range_overlaps("2-4", "1-3"))

    def test_count_contained(self):
        lines = [
            "2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8",
        ]
        self.assertEqual(day4.count_contained(lines), 2)

    def test_count_overlaps(self):
        lines = [
            "2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8",
        ]
        self.assertEqual(day4.count_overlaps(lines), 4)


if __name__ == "__main__":
    unittest.main()
