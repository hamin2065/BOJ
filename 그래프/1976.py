# https://www.acmicpc.net/problem/1976
# 여행 가자

import sys

def find_parent(parent, x) : 
    if parent[x] != x : 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a,b) : 
    a = find_parent(parent,a)
    b = find_parent(parent, b)
    if a < b : parent[b] = a
    else : parent[a] = b

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

for i in range(n) : 
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(n) : 
        # 이미 같은 집합이면 pass
        if find_parent(parent, i+1) == find_parent(parent, j+1) : continue
        # 새로 연결되어야하는 경우
        elif arr[j] == 1 : 
            union(parent,i+1,j+1)

plan = list(map(int, sys.stdin.readline().split()))
a = find_parent(parent,plan[0])
for i in range(1,m) : 
    if a != find_parent(parent, plan[i]) : 
        print("NO")
        exit()
print("YES")