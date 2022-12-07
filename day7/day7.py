import sys


class FileSystemObject:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent


class File(FileSystemObject):
    def __init__(self, name, parent, size):
        self.size = size
        super().__init__(name, parent)

    def print(self):
        return [f"- {self.name} (file, size={self.size})"]


class Directory(FileSystemObject):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.children = []

    def print(self):
        children = [child.print() for child in self.children]
        return [f"- {self.name} (dir)"] + [
            "  " + child for flatten in children for child in flatten
        ]


def build_tree(lines):
    root = Directory("/", None)
    current = root

    for line in lines:
        print(line)
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
                fso = File(name, current, size)
            current.children.append(fso)

    return root


def sum_dir_size(input):
    pass


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        print(sum_dir_size(f.read()))


if __name__ == "__main__":
    main()
