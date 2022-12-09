import sys


def count_visible(line):
    for i in range(len(line) - 1):
        if line[i] < line[i + 1]:
            return i
    return len(line)


def line_of_sight(data):
    rows = [l for l in data.splitlines() if l != ""]
    columns = ["".join(x) for x in zip(*rows)]
    return rows + columns


def part1(input):
    pass


def main():
    with open(sys.argv[0]) as f:
        print(part1(f.read()))


if __name__ == "__main__":
    main()
