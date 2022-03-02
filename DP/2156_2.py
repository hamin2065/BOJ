n = int(input())
arr = [int(input()) for _ in range(n)]
DP = [0]*10000

DP[0] = arr[0]
if n > 1 : 
    DP[1] = arr[0]+arr[1]
if n > 2 : 
    DP[2] = max(DP[1],arr[0]+arr[2],arr[1]+arr[2])

for i in range(3,n) : 
    DP[i] = max(DP[i-1],DP[i-2]+arr[i], DP[i-3]+arr[i]+arr[i-1])
print(max(DP))