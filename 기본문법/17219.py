# https://www.acmicpc.net/problem/17219
# 비밀번호 찾기

from collections import defaultdict

dd = defaultdict(list)

n, m = map(int, input().split())

for _ in range(n) : 
    a,b = input().split()
    dd[a].append(b)
    
for _ in range(m) : 
    print(dd[input()][0])