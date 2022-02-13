# https://www.acmicpc.net/problem/1715
# 카드 정렬하기

import heapq

heap = []

n = int(input())

for _ in range(n) : 
    heapq.heappush(heap, int(input()))
result = 0
while len(heap) >= 2 : 
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result += a+b
    heapq.heappush(heap, a+b)
print(result)
