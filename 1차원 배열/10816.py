# https://www.acmicpc.net/problem/10816
# 숫자 카드 2

import sys

n = int(input())
cards = list(map(int, sys.stdin.readline().strip().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().strip().split()))

dict = {}

for i in cards:
    if i in dict : dict[i] += 1
    else : dict[i] = 1
    
for i in check : 
    if i in dict : 
        print(dict[i], end = ' ')
    else : print(0, end=' ')