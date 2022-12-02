import sys


def total_score_part1(lines):
    return sum(
        (3 if a == b else 6 if (b - 1 or 3) == a else 0) + b
        for a, b in ((ord(a) - 64, ord(b) - 87) for a, b in (l.split() for l in lines))
    )

def total_score_part2(lines):
    return sum(
        (a if b == 2 else a % 3 + 1 if b == 3 else a - 1 or 3) + (b - 1) * 3
        for a, b in ((ord(a) - 64, ord(b) - 87) for a, b in (l.split() for l in lines))
    )

def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.read().splitlines()
    print(total_score_part2(lines))


if __name__ == "__main__":
    main()
