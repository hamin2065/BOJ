# https://www.acmicpc.net/problem/2445
# 별 찍기 - 8

n = int(input())

for i in range(n-1):
    print("*"*(i+1),end='')
    print(" "*(n-1-i),end='')
    print(" "*(n-1-i),end='')
    print("*"*(i+1),end='')
    print()
print("*"*2*n)
for i in range(n-2,-1,-1):
    print("*"*(i+1),end='')
    print(" "*(n-1-i),end='')
    print(" "*(n-1-i),end='')
    print("*"*(i+1),end='')
    print()