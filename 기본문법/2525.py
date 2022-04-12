# https://www.acmicpc.net/problem/2525
# 오븐 시계

a, b = map(int, input().split())
c = int(input())

if b+c >= 60 : 
    a += (b+c)//60
b = (b+c)%60
if a > 23 : a -= 24

print(a, b)