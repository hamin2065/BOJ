from collections import deque

n = int(input())
m = int(input())

visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]

def BFS(v) : 
    result = 0
    que = deque([])
    que.append(v)
    visited[v] = True
    while que : 
        for _ in range(len(que)) : 
            k = que.popleft()
            for i in graph[k] : 
                if visited[i] == False : 
                    visited[i] = True
                    result += 1
                    que.append(i)
    return result
for _ in range(m) : 
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(BFS(1))