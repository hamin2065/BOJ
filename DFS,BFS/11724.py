# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수

from collections import deque

def BFS(graph1,graph2, visited, deq, num) : 
    if visited[num] == True : return
    visited[num] = True
    deq.append(num)
    global cnt
    while deq : 
        curr = deq.popleft()
        for i in graph1[curr] : 
            if visited[i] == False : 
                deq.append(i)
                visited[i] = True
        for i in graph2[curr] : 
            if visited[i] == False : 
                deq.append(i)
                visited[i] = True
    cnt += 1
    
n, m = map(int, input().split())

graph1 = [[]for _ in range(n+1)]
graph2 = [[]for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m) : 
    a,b = map(int, input().split())
    graph1[a].append(b)
    graph2[b].append(a)
    
deq = deque([1])
cnt = 0
for i in range(1,n+1) : 
    BFS(graph1,graph2, visited,deq,i)
    
print(cnt)