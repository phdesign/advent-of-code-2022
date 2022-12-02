import unittest
from day2 import total_score

ROCK = 1
PAPER = 2
SCISSORS = 3

class TestDay2(unittest.TestCase):

    def test_total_score(self):
      lines = ['A Y', 'B X', 'C Z']
      actual = total_score(lines)
      self.assertEqual(actual, 15)

if __name__ == '__main__':
    unittest.main()
