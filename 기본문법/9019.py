# https://www.acmicpc.net/problem/9375
# 패션왕 신해빈

from itertools import combinations
from sys import stdin

n = int(input())

for _ in range(n) : 
    d = {}
    for _ in range(int(stdin.readline())) : 
        s = stdin.readline().split()
        if s[1] in d : 
            d[s[1]] += 1
        else : 
            d[s[1]] = 1
    answer = 1
    for k in d.keys() : 
        answer*=(d[k]+1)
    print(answer-1)