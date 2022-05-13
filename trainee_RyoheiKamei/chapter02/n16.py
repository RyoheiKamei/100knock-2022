
import sys
import math

N: int = int(sys.argv[1])
with open("./data/popular-names.txt", mode="r") as f:
    lines = f.readlines()
    numlines=len(lines)
    n = N
    begin = 0
    while n > 0:
        border = math.ceil(numlines / n)
        end = begin + border
        out = "".join(lines[begin:end])
        print(out, end="---------------------------\n")
        begin += border
        n -= 1
        numlines -= border
