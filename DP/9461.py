# https://www.acmicpc.net/problem/9461
# 파도반 수열

T = int(input())

for _ in range(T) : 
    n = int(input())
    arr = [0,1,1,1,2,2]
    for i in range(6,n+1) : 
        arr.append(arr[i-1]+arr[i-5])
    print(arr[n])