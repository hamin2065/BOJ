# https://www.acmicpc.net/problem/18870
# 좌표 압축

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = list(set(arr))
arr2.sort()

dict = {}

for i in range(len(arr2)) : 
    dict[arr2[i]] = i

for i in range(len(arr)) : 
    print(dict[arr[i]],end=' ')