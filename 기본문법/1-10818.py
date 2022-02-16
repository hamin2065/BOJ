# 최소, 최대
# https://www.acmicpc.net/problem/10818

n = int(input())

a = list(map(int, input().split()))
a.sort()

print(a[0],a[-1])