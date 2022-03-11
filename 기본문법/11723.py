# https://www.acmicpc.net/problem/11723
# 집합

from sys import stdin

S = set()

n = int(input())
for _ in range(n) : 
    com = stdin.readline().strip().split()
    if com[0] == "all" : 
        S = set([i for i in range(1,21)])
    elif com[0] == "add" : 
        S.add(int(com[1]))
    elif com[0] == "remove" : 
        S.discard(int(com[1]))
    elif com[0] == "check" : 
        print(1 if int(com[1]) in S else 0)
    elif com[0] == "toggle" : 
        if int(com[1]) in S : 
            S.discard(int(com[1]))
        else :
            S.add(int(com[1]))
    else : 
        S = set()