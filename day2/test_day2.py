import unittest
from day2 import total_score_part1, total_score_part2

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 1
DRAW = 2
WIN = 3

def score(a, b):
    if a == b:
        return 3
    if (b - 1 or 3) == a:
        return 6
    return 0

def shape(a, b):
    if b == 2:
        return a
    if b == 3:
      return a % 3 + 1
    return a - 1 or 3


class TestDay2(unittest.TestCase):

    def test_total_score_part1(self):
      lines = ['A Y', 'B X', 'C Z']
      actual = total_score_part1(lines)
      self.assertEqual(actual, 15)

    def test_total_score_part2(self):
      lines = ['A Y', 'B X', 'C Z']
      actual = total_score_part2(lines)
      self.assertEqual(actual, 12)

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

    def test_shape(self):
      self.assertEqual(shape(ROCK, WIN), PAPER)
      self.assertEqual(shape(ROCK, DRAW), ROCK)
      self.assertEqual(shape(ROCK, LOSE), SCISSORS)
      self.assertEqual(shape(PAPER, WIN), SCISSORS)
      self.assertEqual(shape(PAPER, DRAW), PAPER)
      self.assertEqual(shape(PAPER, LOSE), ROCK)
      self.assertEqual(shape(SCISSORS, WIN), ROCK)
      self.assertEqual(shape(SCISSORS, DRAW), SCISSORS)
      self.assertEqual(shape(SCISSORS, LOSE), PAPER)

if __name__ == '__main__':
    unittest.main()
