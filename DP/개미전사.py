# 이것이 취업을 위한 코딩테스트다 p.220
# 개미 전사

n = int(input())
arr = list(map(int, input().split()))

dp = [0]*100

dp[0] = arr[0]
dp[1] = max(arr[0],arr[1])

for i in range(2, n) : 
    dp[i] = max(arr[i-1], arr[i-2]+arr[i])
    
print(dp[n-1])