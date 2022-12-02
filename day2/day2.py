import sys


def total_score(lines):
    return sum(
        (3 if a == b else 6 if (b - 1 or 3) == a else 0) + b
        for a, b in ((ord(a) - 64, ord(b) - 87) for a, b in (l.split() for l in lines))
    )


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.read().splitlines()
    print(total_score(lines))


if __name__ == "__main__":
    main()
