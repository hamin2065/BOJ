# https://www.acmicpc.net/problem/10953
# A+B - 6

n = int(input())
for i in range(n):
    a,b = map(int, input().split(','))
    print(a+b)