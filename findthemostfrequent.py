
import sys
import math
from collections import Counter

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

words = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
f = Counter(words)
del(f[" "])
x = max(f.values())
for i in f.keys():
    if f[i] == x:
        print(f[i])
        break
