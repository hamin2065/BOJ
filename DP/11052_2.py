n = int(input())
cards = [0]+list(map(int, input().split()))
DP = [0]*(n+1)
for i in range(1,n+1) : 
    for j in range(1,i+1) : 
        if DP[i] < DP[i-j]+cards[j] : 
            DP[i] = DP[i-j]+cards[j]
print(DP[n])