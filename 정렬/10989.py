# https://www.acmicpc.net/problem/10989
# 수 정렬하기 3

import sys
input = sys.stdin.readline

n = int(input())
arr=[0]*10001
for _ in range(n):
    num = int(input())
    arr[num] += 1

for i in range(len(arr)):
    while arr[i] != 0:
        print(i)
        arr[i] -= 1