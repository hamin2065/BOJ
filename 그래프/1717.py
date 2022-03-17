# https://www.acmicpc.net/problem/1717
# 집합의 표현
import sys
sys.setrecursionlimit(10**5)
def find_parent(parent, x) : 
    if parent[x] != x : 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent,a,b) : 
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b : parent[b] = a
    else : parent[a] = b
    
n,m = map(int, input().split())

parent = [i for i in range(n+1)]

for _ in range(m) : 
    a,b,c = map(int, sys.stdin.readline().split())
    if a == 0 : 
        union(parent,b,c)
    else : 
        if find_parent(parent,b) == find_parent(parent,c) : 
            print("YES")
        else : print("NO")