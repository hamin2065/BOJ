# https://www.acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 법칙

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
link = [[] for _ in range(n+1)]

def BFS(num) : 
    arr = [0 for _ in range(n+1)]
    visited = [num]
    que = deque()
    que.append(num)
    
    while que :
        k = que.popleft()
        for i in link[k] : 
            if i not in visited : 
                arr[i] = arr[k] + 1
                visited.append(i)
                que.append(i)
                
    return sum(arr)


for _ in range(m):
    a,b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
    
result = []
for num in range(1,n+1) :
    result.append(BFS(num))
    
print(result.index(min(result))+1)