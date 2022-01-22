# https://www.acmicpc.net/problem/1654
# 랜선 자르기

from sys import stdin
n,k = map(int, stdin.readline().strip().split())
lines = [int(stdin.readline().strip()) for _ in range(n)]

start = 1;end = max(lines)
while start <= end : 
    mid = (start + end) // 2
    total = 0
    for i in lines:
        total += i//mid
    if total >= k : 
        start = mid + 1
    else : 
        end = mid-1
print(end)