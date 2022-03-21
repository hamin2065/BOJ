from collections import deque

def BFS(graph1, start, visited1) : 
    que = deque([start])    
    visited1[start] = True
    while que:
        v = que.popleft()
        print(v,end=' ')
        for i in graph1[v] : 
            if not visited1[i] : 
                que.append(i)
                visited1[i] = True
                
def DFS(graph2,v,visited2) : 
    visited2[v] = True
    print(v,end=' ')
    for i in graph2[v] : 
        if not visited2[i] : 
            DFS(graph2, i,visited2)
            
n,m,v = map(int, input().split())

visited1 = [False]*(n+1)
visited2 = [False]*(n+1)

graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

for _ in range(m) : 
    a,b=map(int, input().split())
    graph1[a].append(b)
    graph1[b].append(a)
    graph2[a].append(b)
    graph2[b].append(a)
    
DFS(graph2,v,visited2)
print()
BFS(graph1,v,visited1)