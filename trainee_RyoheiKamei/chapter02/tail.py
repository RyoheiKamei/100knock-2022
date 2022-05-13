import sys
from collections import deque

if len(sys.argv) != 3:
    print("Usage: tail.py NUM FILE", file=sys.stderr)
    print("Print the last NUM lines of FILE to standard output.", file=sys.stderr)
    sys.exit()

n_lines = int(sys.argv[1])
file = sys.argv[2]
for line in deque(open(file), n_lines):
    print(line, end="")
