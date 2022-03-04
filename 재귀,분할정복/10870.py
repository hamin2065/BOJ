# 피보나치 수 5
# https://www.acmicpc.net/problem/10870

def fibo(num):
    if num <= 1:return num
    return fibo(num-1)+fibo(num-2)

print(fibo(int(input())))