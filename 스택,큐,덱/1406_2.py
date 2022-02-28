from sys import stdin
from collections import deque

right = [];left = list(input())

n = int(input())

for _ in range(n) : 
    c = stdin.readline().strip().split()
    if c[0] =="L" :
        if left : 
            right.append(left.pop())
    elif c[0] == "D" :
        if right : 
            left.append(right.pop())
    elif c[0] == "B" : 
        if left : 
            left.pop()
    elif c[0] == "P" : 
        left.append(c[1])
print("".join(left[:]+right[::-1]))

