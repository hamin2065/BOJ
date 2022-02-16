# https://www.acmicpc.net/problem/10991
# 별 찍기 - 16

n = int(input())

for i in range(n):
    print(" "*(n-i-1),end='')
    print("* "*(i+1),end='')
    print()