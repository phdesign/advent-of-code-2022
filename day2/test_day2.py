import unittest
from day2 import total_score, score

ROCK = 1
PAPER = 2
SCISSORS = 3

class TestDay2(unittest.TestCase):

    def test_total_score(self):
      lines = ['A Y', 'B X', 'C Z']
      actual = total_score(lines)
      self.assertEqual(actual, 15)

    def test_score(self):
      self.assertEqual(score(ROCK, ROCK), 3)
      self.assertEqual(score(ROCK, PAPER), 6)
      self.assertEqual(score(ROCK, SCISSORS), 0)
      self.assertEqual(score(PAPER, ROCK), 0)
      self.assertEqual(score(PAPER, PAPER), 3)
      self.assertEqual(score(PAPER, SCISSORS), 6)
      self.assertEqual(score(SCISSORS, ROCK), 6)
      self.assertEqual(score(SCISSORS, PAPER), 0)
      self.assertEqual(score(SCISSORS, SCISSORS), 3)

if __name__ == '__main__':
    unittest.main()
