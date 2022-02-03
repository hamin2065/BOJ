# https://www.acmicpc.net/problem/2178
# 미로 탐색

import sys
from collections import deque

que = deque([('0','0')])

n,m = map(int, input().split())
graph = []
for _ in range(n) : 
    graph.append(list(sys.stdin.readline().strip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS() : 
    while que : 
        x, y = que.popleft()
        for i in range(4) : 
            fx = int(x) + dx[i]
            fy = int(y) + dy[i]
            
            if fx < 0 or fx >= n or fy < 0 or fy >= m : 
                continue
            if graph[fx][fy] == '0' : 
                continue
            if graph[fx][fy] == '1' : 
                graph[fx][fy] = str(int(graph[int(x)][int(y)])+1)
                que.append((fx, fy))
    return graph[int(n)-1][int(m)-1]

print(BFS())