#Input:abcadxad
#Output:x


import sys
import math


s = input()
for c in s:
    if s.count(c)==1:
        input(c)

print("_")

//////////////////////////////

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
r= ""
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for i in s:
    if(s.count(i) == 1):
        r = i
        break
    else:
        r = "_"
print(r)


////////////




s = input()

ch = ""
for j in s:
    results = [i for i, x in enumerate(s) if x == j]
    if len(results) == 1:
        ch = j
        break

if ch != "":
    print(ch)
else:
    print("_")