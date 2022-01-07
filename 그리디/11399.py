# https://www.acmicpc.net/problem/11399
# ATM

n = int(input())
times = list(map(int, input().split()))

times.sort()

result = 0
for i in range(n):
    result += times[i]*(n-i)
print(result)