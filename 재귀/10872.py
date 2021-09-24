# 팩토리얼
# https://www.acmicpc.net/problem/10872

def rec(num):
    if num <= 1:return 1
    return num*rec(num-1)

print(rec(int(input())))