n = int(input())
arr = list(map(int, input().split()))

DP = [1]*n
# 각자 자리에 자신을 기준으로 앞에 수열중에 자신보다 작은거 집어넣기
for i in range(len(arr)) : 
    for j in range(i) : 
        if arr[j] < arr[i] : 
            DP[i] = max(DP[i],DP[j]+1)

print(max(DP))