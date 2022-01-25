# https://www.acmicpc.net/problem/11286
# 절댓값 힙

from sys import stdin
import heapq

heap_p = []
heap_n = []

n = int(stdin.readline().strip())
for i in range(n) : 
    num = int(stdin.readline().strip())
    if num < 0 : 
        heapq.heappush(heap_n,-num)
    elif num == 0 : 
        if len(heap_p) == 0 and len(heap_n) == 0: 
            print(0)
        elif len(heap_p) == 0 : print(-heapq.heappop(heap_n))
        elif len(heap_n) == 0 : print(heapq.heappop(heap_p))
        else : 
            if heap_p[0] >= heap_n[0] : print(-heapq.heappop(heap_n))
            else:print(heapq.heappop(heap_p))
    else : 
        heapq.heappush(heap_p,num)