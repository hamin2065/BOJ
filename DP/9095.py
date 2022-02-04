# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기

arr = [1,2,4]
for i in range(3,10) : 
    arr.append(arr[i-3]+arr[i-2]+arr[i-1])

n = int(input())
for i in range(n) : 
    num = int(input())
    print(arr[num-1])