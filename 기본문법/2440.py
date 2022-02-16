# https://www.acmicpc.net/problem/2440
# 별 찍기 - 3

n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end='')
    print()