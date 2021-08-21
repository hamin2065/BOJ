# 소수 구하기
# https://www.acmicpc.net/problem/1929

import math
def prime(n):
    if n <= 1:return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:return False
    return True

a,b = map(int, input().split())
print("\n".join(str(i) for i in range(a,b+1) if prime(i) == True))