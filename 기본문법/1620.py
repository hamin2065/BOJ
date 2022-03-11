# https://www.acmicpc.net/problem/1620
# 나는야 포켓몬 마스터 이다솜
import sys
n, m = map(int, input().split())

dict1 = {}
dict2 = {}

for i in range(n) : 
    s = sys.stdin.readline().strip()
    dict1[s] = i+1
    dict2[i+1] = s
    
for i in range(m) : 
    s = sys.stdin.readline().strip()
    if s.isdigit() : 
        print(dict2[int(s)])
    else : 
        print(dict1[s])