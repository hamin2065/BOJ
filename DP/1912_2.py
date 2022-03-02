n = int(input())
arr = list(map(int, input().split()))

DP = [0]*n
DP[0] = arr[0]

for i in range(1,n) : 
    DP[i] = max(arr[i],DP[i-1]+arr[i])
    
print(max(DP))