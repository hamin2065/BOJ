# OX퀴즈
# https://www.acmicpc.net/problem/8958

def score(A):
    a = result = 0
    for i in range(len(A)):
        if A[i] == 'O':
            a += 1
            result += a
        else:
            a = 0
    return result
n = int(input())

for _ in range(n):
    A = input()
    print(score(A))
    