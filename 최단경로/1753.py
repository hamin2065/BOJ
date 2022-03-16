# https://www.acmicpc.net/problem/1753
# 최단 경로

import heapq
from sys import stdin

INF = int(1e9)

v, e = map(int, input().split())

start = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)

for _ in range(e) : 
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b,c))

def solve(start) : 
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q : 
        dis, node = heapq.heappop(q)
        if distance[node] < dis : continue
        for i in graph[node] : 
            cost = dis + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (distance[i[0]], i[0]))
solve(start)
for i in range(1, v+1) : 
    if distance[i] == INF : 
        print("INF")
    else : 
        print(distance[i])