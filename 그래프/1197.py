# https://www.acmicpc.net/problem/1197
# 최소 스패닝 트리
import sys
def find_parent(parent, x) : 
    if parent[x] != x : 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b) : 
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b : parent[b] = a
    else : parent[a] = b
    
v, e = map(int, input().split())
arr = []
parent = [i for i in range(v+1)]
for _ in range(e) : 
    a,b,cost = map(int, sys.stdin.readline().split())
    arr.append((cost,a,b))
arr.sort()
result = 0
for edge in arr : 
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) : 
        union(parent,a,b)
        result += cost
        
print(result)