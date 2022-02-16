# X보다 작은 수
# https://www.acmicpc.net/problem/10871

n, x = map(int, input().split())

A = list(map(int, input().split()))
a = ''
for i in range(len(A)):
    if A[i] < x : a += (str(A[i]) + ' ')
print(a)