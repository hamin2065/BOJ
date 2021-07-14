# 나머지
# https://www.acmicpc.net/problem/10430

A,B,C = map(int, input().split())

print(f'{(A+B)%C}\n{((A%C) + (B%C))%C}\n{(A*B)%C}\n{((A%C) * (B%C))%C}')