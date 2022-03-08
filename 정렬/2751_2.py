n = int(input())
A = [int(input()) for _ in range(n)]

A.sort()
for i in range(n) : print(A[i])