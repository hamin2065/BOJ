n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

remains = k
count = 0

for i in range(n-1,-1,-1) : 
    if coins[i] <= remains : 
        k = remains//coins[i]
        remains -= (k*coins[i])
        count += k
    else : pass
print(count)