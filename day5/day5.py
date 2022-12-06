import sys
import re


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


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.read().splitlines()
    # result = count_overlaps(lines)
    # print(result)


if __name__ == "__main__":
    main()
