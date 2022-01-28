# https://www.acmicpc.net/problem/1912
# 연속합

from sys import stdin

n = int(stdin.readline().strip())
num = list(map(int, stdin.readline().strip().split()))
dp = [0 for _ in range(n)]
dp[0] = num[0]

for i in range(1,n) : 
    dp[i] = max(dp[i-1]+num[i],num[i])
print(max(dp))