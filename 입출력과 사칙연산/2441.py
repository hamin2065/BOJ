# https://www.acmicpc.net/problem/2441
# 별 찍기 - 4

n = int(input())

for i in range(n):
    print(" "*i,end='')
    print("*"*(n-i),end='')
    print()