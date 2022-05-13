import sys
from itertools import islice

if len(sys.argv) != 3:
    print("Usage: head.py NUM FILE", file=sys.stderr)
    print("Print the first NUM lines of FILE to standard output.", file=sys.stderr)
    sys.exit()

n_lines = int(sys.argv[1])
file = sys.argv[2]
for line in islice(open(file), n_lines):
    print(line, end="")
