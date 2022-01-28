# https://www.acmicpc.net/problem/1149
# RGB 거리

from sys import stdin
n = int(input())
h = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]

dp = [[0 for _ in range(3)] for _ in range(n)]

dp[0] = h[0]

for i in range(1,n) : 
    dp[i][0] = min(dp[i-1][1]+h[i][0],dp[i-1][2]+h[i][0])
    dp[i][1] = min(dp[i-1][0]+h[i][1],dp[i-1][2]+h[i][1])
    dp[i][2] = min(dp[i-1][0]+h[i][2],dp[i-1][1]+h[i][2])
    
print(min(dp[n-1]))