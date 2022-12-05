import sys


def find_duplicate(line):
    first_half, second_half = line[: len(line) // 2], line[len(line) // 2 :]
    return next((c for c in first_half if c in second_half), None)


def find_badge(group):
    sets = (set(line) for line in group)
    return list(set.intersection(*sets))[0]


def priority(char):
    return (
        ord(char) - ord("A") + 27
        if char.isupper()
        else ord(char) - ord("a") + 1
    )


def priority_sum(lines):
    duplicates = [find_duplicate(line) for line in lines]
    return sum(priority(item) for item in duplicates if item)


def badge_priority_sum(lines):
    badges = (find_badge(lines[i : i + 3]) for i in range(0, len(lines), 3))
    return sum(priority(item) for item in badges if item)


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.read().splitlines()
    # result = priority_sum(lines)
    result = badge_priority_sum(lines)
    print(result)


if __name__ == "__main__":
    main()
