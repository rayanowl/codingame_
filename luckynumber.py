#Lucky Number


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

number = (input())
l = False
if "6" in number:
    l = True
if "8" in number:
    l = not l
print("Lucky" if l else "Not Lucky")