# https://www.acmicpc.net/problem/4386
# 별자리 만들기
from sys import stdin
import math

def find_parent(parent, x) : 
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b) : 
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b : parent[b] = a
    else : parent[a] = b

n = int(input())
parent = [i for i in range(n+1)]
star = []

for _ in range(n) :
    x, y = map(float, stdin.readline().split()) 
    star.append((x,y))

arr = []
for i in range(n) : 
    for j in range(n) : 
        if i != j : 
            dis = math.sqrt((star[i][0]-star[j][0])**2 + (star[i][1]-star[j][1])**2)
            arr.append((dis, i,j))

arr.sort()
result = 0
for s in arr : 
    cost, a, b = s
    if find_parent(parent,a) != find_parent(parent, b) : 
        result += cost
        union(parent, a, b)
print(result)