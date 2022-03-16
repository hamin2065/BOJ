# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로

import heapq
from sys import stdin

INF = int(1e9)

n, e = map(int, input().split())

graph = [[]for _ in range(n+1)]

for _ in range(e) : 
    a,b,c = map(int, stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int, input().split())
def solve(st) : 
    q = []
    distance=[INF for _ in range(n+1)]
    heapq.heappush(q, (0,st))
    distance[st] = 0
    while q : 
        dis, node = heapq.heappop(q)
        if distance[node] < dis : continue
        for i in graph[node] : 
            cost = dis + i[1]
            if cost < distance[i[0]] : 
                distance[i[0]] = cost
                heapq.heappush(q, (distance[i[0]], i[0]))
    return distance

arr_first = solve(1)
arr_second = solve(v1)
arr_third = solve(v2)

result = min(arr_first[v1]+arr_second[v2]+arr_third[n], arr_first[v2]+arr_third[v1]+arr_second[n])
print(result if result < INF else -1)

