# 소인수분해
# https://www.acmicpc.net/problem/11653
import math
def prime(n):
    if n <= 1:return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:return False
    return True

n = int(input())
i = 2
while n != 1:
    if n % i == 0 and prime(i) == True:
        print(i)
        n //= i
    else:i+=1

