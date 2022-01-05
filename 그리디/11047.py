# https://www.acmicpc.net/problem/11047
# 동전 0

n, k = map(int, input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))
i = n-1
result = 0
while k != 0:
    if k < coins[i]:
        i -= 1
        continue
    result += (k//coins[i])
    k = k%coins[i]
    i -= 1
print(result)

