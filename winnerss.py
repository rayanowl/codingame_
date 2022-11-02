# Who is the winner?


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
ia, ib, a_1, b_1 = [int(i) for i in input().split()]
a=ia
b=ib

for i in range(r):
    a -= b_1
    b+= b_1//2
    if a <= 0:
        print("B", b)
        exit()

    b -= a_1
    a+=a_1//2

    if b <= 0:
        print("A", a)
        exit()


if a > b:
    print("A", a)
else:
    print("B", b)


////////////////////////////////

