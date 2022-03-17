# https://www.acmicpc.net/problem/20040
# 사이클 게임

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
    
n, m = map(int, input().split())
parent = [i for i in range(n)]
result = 0
for i in range(m) : 
    x, y = map(int, sys.stdin.readline().split())
    if find_parent(parent, x) == find_parent(parent, y) and result == 0 : 
        result = i+1
    union(parent, x, y)
print(result)