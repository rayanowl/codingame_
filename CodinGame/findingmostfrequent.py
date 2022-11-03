# Finding the most frequent character in a string


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


///////////////////////



words = input()
dictio = {}
for i in words : 
    if i != " " : 
        if i not in dictio:
            dictio[i] = 1
        else :
            dictio[i] += 1

maxi = 0
for i in dictio.values() :
    if i > maxi :
        maxi = i 

print(maxi)