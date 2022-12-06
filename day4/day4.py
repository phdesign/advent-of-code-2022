import sys


def range_contains(a, b):
    a_start, a_end = (int(i) for i in a.split("-"))
    b_start, b_end = (int(i) for i in b.split("-"))
    return (a_start <= b_start and a_end >= b_end) or (
        a_start >= b_start and a_end <= b_end
    )


def range_overlaps(a, b):
    a_start, a_end = (int(i) for i in a.split("-"))
    b_start, b_end = (int(i) for i in b.split("-"))
    return (
        (a_start <= b_start <= a_end)
        or (a_start <= b_end <= a_end)
        or (b_start <= a_start <= b_end)
        or (b_start <= a_end <= b_end)
    )


def count_contained(lines):
    return sum(range_contains(*line.split(",")) for line in lines)


def count_overlaps(lines):
    return sum(range_overlaps(*line.split(",")) for line in lines)


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.read().splitlines()
    result = count_overlaps(lines)
    print(result)


if __name__ == "__main__":
    main()
