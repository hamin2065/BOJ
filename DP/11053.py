# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열

n = int(input())
arr = list(map(int, input().split()))

DP = [1 for _ in range(n)]


for i in range(n) : 
    for j in range(i) : 
        if arr[j] < arr[i] : 
            DP[i] = max(DP[i], DP[j]+1)
        
print(max(DP))