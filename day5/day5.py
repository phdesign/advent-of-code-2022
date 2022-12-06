import sys
import re
from operator import itemgetter


def get_moves(lines):
    return [
        {
            "count": int(m.group(1)),
            "from": int(m.group(2)),
            "to": int(m.group(3)),
        }
        for m in (
            re.search(r"^move (\d+) from (\d+) to (\d+)", line)
            for line in lines
        )
        if m
    ]


def get_stacks(lines):
    columns = [m.start() for m in re.finditer(r"\d+", lines.pop())]
    return [
        [
            line[column]
            for line in reversed(lines)
            if len(line) >= column and line[column] != " "
        ]
        for column in columns
    ]


def reorder_stacks(stacks, moves):
    for move in moves:
        for _ in range(move["count"]):
            stacks[move["to"] - 1].append(stacks[move["from"] - 1].pop())


def reorder_stacks_9001(stacks, moves):
    for move in moves:
        count, src, dest = itemgetter("count", "from", "to")(move)
        stacks[dest - 1].extend(stacks[src - 1][-count:])
        stacks[src - 1] = stacks[src - 1][: len(stacks[src - 1]) - count]


def top_crates(input, reorder):
    stack_string, move_string = input.split("\n\n")
    stacks = get_stacks(stack_string.splitlines())
    moves = get_moves(move_string.splitlines())
    reorder(stacks, moves)
    return "".join([s[-1] for s in stacks])


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        print(top_crates(f.read(), reorder_stacks_9001))


if __name__ == "__main__":
    main()
