# 소수 찾기
# https://www.acmicpc.net/problem/1978
import math
def prime(n):
    if n <= 1:return True
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:return True
    return False

n = int(input())
prime_num = list(map(int, input().split()))
a = 0
for i in prime_num:
    if prime(i) == False:a += 1
print(a)