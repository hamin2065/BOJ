# 별 찍기 - 1
# https://www.acmicpc.net/problem/2438

n = int(input())
for i in range(n):
    for _ in range(i+1):print("*",end='')
    print()