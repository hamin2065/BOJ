# https://www.acmicpc.net/problem/2217
# 로프

from sys import stdin
n = int(input())
rope = [int(stdin.readline().strip()) for _ in range(n)]

rope.sort()

current = 0

for i in range(n) : 
    if current <= rope[i]*(n-i) : 
        current = rope[i]*(n-i)
print(current)