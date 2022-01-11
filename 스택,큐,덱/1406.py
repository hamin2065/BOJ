# https://www.acmicpc.net/problem/1406
# 에디터

import sys
left = list(sys.stdin.readline().strip())
n = int(input())
right = []

for i in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == "L":
        if len(left) == 0 : continue
        right.append(left.pop())
    elif command[0] == "D":
        if len(right) == 0 : continue
        left.append(right.pop())
    elif command[0] == "B":
        if len(left) == 0 : continue
        left.pop()
    else:#P인 경우
        left.append(command[1])
print("".join(left[:]+right[::-1]))