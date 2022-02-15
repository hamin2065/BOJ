# https://www.acmicpc.net/problem/11052
# 카드 구매하기

n = int(input())
cards = [0] + list(map(int, input().split()))

DP = [0 for _ in range(n+1)]

DP[0] = cards[0]

for i in range(1,n+1) : 
    for j in range(1, i+1) : 
        if DP[i] < DP[i-j] + cards[j] : 
            DP[i] = DP[i-j] + cards[j]
            
print(DP[n])