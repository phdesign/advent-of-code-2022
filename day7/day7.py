import sys
from itertools import chain

TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000


class FileSystemObject:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0


class File(FileSystemObject):
    def __init__(self, name, parent, size):
        super().__init__(name, parent)
        self.size = size

    def tostring(self):
        return f"- {self.name} (file, size={self.size})\n"


class Directory(FileSystemObject):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.children = []

    def tostring(self):
        children = (child.tostring().splitlines() for child in self.children)
        return f"- {self.name} (dir)\n" + "\n".join(
            ["  " + child for sublist in children for child in sublist]
        )


def build_tree(lines):
    root = Directory("/", None)
    current = root

    for line in lines:
        if line.startswith("$ cd"):
            path = line[5:]
            if path == "/":
                current = root
            elif path == "..":
                current = current.parent
            else:
                current = next(
                    d
                    for d in current.children
                    if d.name == path and isinstance(d, Directory)
                )

        elif line.startswith("$ ls"):
            pass

        elif line:
            size, name = line.split()
            if size == "dir":
                fso = Directory(name, current)
            else:
                fso = File(name, current, int(size))
            current.children.append(fso)

    return root


def calculate_size(branch):
    directories = (d for d in branch.children if isinstance(d, Directory))
    for d in directories:
        calculate_size(d)
    branch.size = sum(c.size for c in branch.children)


def sum_small_dirs(branch):
    child_sum = sum(
        sum_small_dirs(d) for d in branch.children if isinstance(d, Directory)
    )
    return branch.size + child_sum if branch.size <= 100000 else child_sum


def get_dir_sizes(branch):
    return [branch.size] + list(
        chain.from_iterable(
            get_dir_sizes(d)
            for d in branch.children
            if isinstance(d, Directory)
        )
    )


def closest_size(tree, size):
    return next(iter(sorted(s for s in get_dir_sizes(tree) if s > size)), None)


def part1(input):
    tree = build_tree(input.splitlines())
    calculate_size(tree)
    return sum_small_dirs(tree)


def part2(input):
    tree = build_tree(input.splitlines())
    calculate_size(tree)
    needed_space = REQUIRED_SPACE - (TOTAL_SPACE - tree.size)
    return closest_size(tree, needed_space)


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        print(part2(f.read()))


if __name__ == "__main__":
    main()
