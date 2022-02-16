# 숫자의 합
# https://www.acmicpc.net/problem/11720

n = int(input())
N = input()
sum = 0
for i in range(n):
    sum += int(N[i])

print(sum)
