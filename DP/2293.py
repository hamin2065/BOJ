# https://www.acmicpc.net/problem/2293
# 동전 1

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

DP = [0 for _ in range(k+1)]
DP[0] = 1

for coin in coins : 
    for j in range(coin, k+1) : 
        print("DP",DP)
        DP[j] += DP[j-coin]
print(DP[k])