import sys

def score(a, b):
  if a == b:
    return 3
  if (b - 1 or 3) == a:
    return 6
  return 0


def total_score(lines):
  return sum(
    (3 if a == b else 6 if (b - 1 or 3) == a else 0) + b for a, b in
    (
      (ord(a) - 64, ord(b) - 87) for a, b in
      (l.split() for l in lines)
    )
    )

def main():
  filename = sys.argv[1]
  with open(filename) as f:
    lines = f.read().splitlines()
  print(lines)

if __name__ == "__main__":
  main()

