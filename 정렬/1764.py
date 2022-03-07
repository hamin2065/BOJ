# https://www.acmicpc.net/problem/1764
# 듣보잡

from sys import stdin

n, m = map(int, input().split())

arr1 = [stdin.readline().strip() for _ in range(n)]
arr2 = [stdin.readline().strip() for _ in range(m)]
arr = []

arr1.sort()
arr2.sort()
i = 0;j = 0

while True : 
    if i == len(arr1) or j == len(arr2) : break
    if arr1[i] == arr2[j] : 
        arr.append(arr1[i])
        i += 1;j += 1
    elif arr1[i] < arr2[j] : 
        i += 1
    else : 
        j += 1
        
        
print(len(arr))
print("\n".join(sorted(arr)))