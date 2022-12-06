import unittest
from day5 import (
    get_stacks,
    get_moves,
    reorder_stacks,
    reorder_stacks_9001,
    top_crates,
)


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

    def test_get_moves(self):
        input = """
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
        moves = get_moves(input.splitlines())
        self.assertEqual(moves[0], {"count": 1, "from": 2, "to": 1})
        self.assertEqual(moves[1], {"count": 3, "from": 1, "to": 3})
        self.assertEqual(moves[2], {"count": 2, "from": 2, "to": 1})
        self.assertEqual(moves[3], {"count": 1, "from": 1, "to": 2})

    def test_reorder_stacks(self):
        stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]
        moves = [{"count": 1, "from": 2, "to": 1}]
        reorder_stacks(stacks, moves)
        self.assertEqual(stacks, [["Z", "N", "D"], ["M", "C"], ["P"]])

        moves = [{"count": 3, "from": 1, "to": 3}]
        reorder_stacks(stacks, moves)
        self.assertEqual(stacks, [[], ["M", "C"], ["P", "D", "N", "Z"]])

        moves = [{"count": 2, "from": 2, "to": 1}]
        reorder_stacks(stacks, moves)
        self.assertEqual(stacks, [["C", "M"], [], ["P", "D", "N", "Z"]])

        moves = [{"count": 1, "from": 1, "to": 2}]
        reorder_stacks(stacks, moves)
        self.assertEqual(stacks, [["C"], ["M"], ["P", "D", "N", "Z"]])

    def test_reorder_stacks_9001(self):
        stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]
        moves = [{"count": 1, "from": 2, "to": 1}]
        reorder_stacks_9001(stacks, moves)
        self.assertEqual(stacks, [["Z", "N", "D"], ["M", "C"], ["P"]])

        moves = [{"count": 3, "from": 1, "to": 3}]
        reorder_stacks_9001(stacks, moves)
        self.assertEqual(stacks, [[], ["M", "C"], ["P", "Z", "N", "D"]])

    def test_top_crates(self):
        input = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
        self.assertEqual(top_crates(input, reorder_stacks), "CMZ")

    def test_top_crates_9001(self):
        input = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
        self.assertEqual(top_crates(input, reorder_stacks_9001), "MCD")


if __name__ == "__main__":
    unittest.main()
