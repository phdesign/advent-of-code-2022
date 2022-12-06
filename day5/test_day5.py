import unittest
from day5 import get_stacks


class TestSuite(unittest.TestCase):
    def test_get_stacks(self):
        input = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""
        stacks = get_stacks(input.splitlines())
        self.assertEqual(stacks[0], ["Z", "N"])
        self.assertEqual(stacks[1], ["M", "C", "D"])
        self.assertEqual(stacks[2], ["P"])


if __name__ == "__main__":
    unittest.main()
