import sys


def all_shorter(seq, comparison):
    return all(comparison > item for item in seq)


def part1(data):
    count = 0
    matrix = [list(line) for line in data.splitlines() if line != ""]
    print(f"width: {len(matrix[0])}, height: {len(matrix)}")
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            tree = matrix[y][x]
            left = list(reversed(matrix[y][:x]))
            right = matrix[y][x + 1 :]
            top = list(reversed([matrix[i][x] for i in range(y)]))
            bottom = [matrix[i][x] for i in range(y + 1, len(matrix))]
            count += int(
                all_shorter(left, tree)
                or all_shorter(right, tree)
                or all_shorter(top, tree)
                or all_shorter(bottom, tree)
            )
    return count


def main():
    with open(sys.argv[1]) as f:
        print(part1(f.read()))


if __name__ == "__main__":
    main()
