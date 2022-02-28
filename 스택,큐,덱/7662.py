# https://www.acmicpc.net/problem/7662
# 이중 우선순위 큐

import sys
import heapq

n = int(input())
h = []
for _ in range(n) : 
    k = int(input())
    visited = [False]*1000001
    minH, maxH = [],[]
    for i in range(k) : 
        com = sys.stdin.readline().split()
        com[1] = int(com[1])
        if com[0] == "I" : 
            heapq.heappush(minH, (com[1],i))
            heapq.heappush(maxH, (-com[1],i))
            visited[i] = True
                
        elif com[1] == 1 : 
            while maxH and not visited[maxH[0][1]] : heapq.heappop(maxH)
            if maxH : 
                visited[maxH[0][1]] = False
                heapq.heappop(maxH)
        else : 
            while minH and not visited[minH[0][1]] : heapq.heappop(minH)
            if minH : 
                visited[minH[0][1]] = False
                heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]] : heapq.heappop(maxH)
    while minH and not visited[minH[0][1]] : heapq.heappop(minH)
    if maxH and minH : 
        print(-maxH[0][0], minH[0][0])
    else : 
        print("EMPTY")