# https://www.acmicpc.net/problem/2805
# 나무 자르기

from sys import stdin

n, m = map(int, stdin.readline().strip().split())
tree = [*map(int, stdin.readline().strip().split())]

start = 0;end = max(tree);result = 0
while start <= end : 
    mid = (start + end) // 2
    total = sum(x-mid for x in tree if x > mid)
    if total < m : 
        end = mid - 1
    else : 
        start = mid + 1
        
print(end)