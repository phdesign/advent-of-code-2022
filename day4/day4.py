import sys


def range_contains(a, b):
    pass


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.read().splitlines()
    # result = badge_priority_sum(lines)
    # print(result)


if __name__ == "__main__":
    main()
