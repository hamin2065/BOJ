# https://www.acmicpc.net/problem/11652
# 카드

n = int(input())

arr = [int(input()) for _ in range(n)]

arr.sort()

count = [[arr[0],1]]
for i in range(1,n) : 
    if arr[i-1] == arr[i] : 
        count[-1][1] += 1
    else : 
        count.append([arr[i],1])

count.sort(key = lambda x : (-x[1],x[0]))

print(count[0][0])