# https://www.acmicpc.net/problem/4195
# 친구 네트워크

import sys
from collections import defaultdict

def find_parent(parent, x) : 
    if parent[x] != x : 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a,b) : 
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b : return
    elif a < b : parent[b] = a
    else : parent[a] = b

# {key : value} => key = 나 value = 우리 그룹의 루트

for _ in range(int(input())) : 
    F = int(sys.stdin.readline())
    parent = defaultdict(None)
    for _ in range(F) : 
        a,b = sys.stdin.readline().split() 
        if a not in parent : parent[a] = a
        if b not in parent : parent[b] = b
        x = find_parent(parent, a)
        y = find_parent(parent, b)
        count = 0
        for i in parent.keys() : 
            if parent[i] == parent[a] or parent[i] == parent[b] : 
                count += 1
        union(parent,a,b)
        print(count)