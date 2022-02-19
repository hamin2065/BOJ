# https://www.acmicpc.net/problem/2156
# 포도주 시식

from sys import stdin

n = int(input())
drinks = [int(stdin.readline().strip()) for _ in range(n)]

DP = [0 for _ in range(10000)]
DP[0] = drinks[0]
if n > 1 : 
    DP[1] = drinks[0] + drinks[1]
if n > 2 : 
    DP[2] = max(DP[1], drinks[0]+drinks[2],drinks[1]+drinks[2])
for i in range(3, n) : 
    DP[i] = max(DP[i-1],DP[i-3]+drinks[i-1]+drinks[i], DP[i-2]+drinks[i])

print(max(DP))
