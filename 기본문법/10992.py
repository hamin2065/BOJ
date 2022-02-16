# https://www.acmicpc.net/problem/10992
# 별 찍기 - 17

n = int(input())

for i in range(0,n-1):
    print(" "*(n-1-i),end='')
    print("*",end='')
    print(" "*(2*i-1),end='')
    if i != 0 : print("*",end='')
    print()
print("*"*(2*n-1))