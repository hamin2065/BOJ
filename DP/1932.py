# https://www.acmicpc.net/problem/1932
# 정수 삼각형

from sys import stdin

n = int(stdin.readline().strip())
tri = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[n-1] = tri[n-1]


for i in range(n-2,-1,-1) : 
    for j in range(len(tri[i])) : 
        dp[i][j] = max(dp[i+1][j]+tri[i][j], dp[i+1][j+1]+tri[i][j])
print(dp[0][0])