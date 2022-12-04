import unittest
import day3


class TestDay2(unittest.TestCase):
    def test_priority_sum(self):
        lines = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]
        actual = day3.priority_sum(lines)
        self.assertEqual(actual, 157)

    def test_find_duplicate(self):
        self.assertEqual(day3.find_duplicate("vJrwpWtwJgWrhcsFMMfFFhFp"), "p")

    def test_priority(self):
        self.assertEqual(day3.priority("a"), 1)
        self.assertEqual(day3.priority("z"), 26)
        self.assertEqual(day3.priority("A"), 27)
        self.assertEqual(day3.priority("Z"), 52)


if __name__ == "__main__":
    unittest.main()
