# 베르트랑 공준
# https://www.acmicpc.net/problem/4948

import math

def prime_list(n):
    sieve = [True] * (2*n+1)
    for i in range(2, int(math.sqrt(2*n)) + 1):
        if sieve[i] == True:
            for j in range(2*i, 2*n+1, i): 
                sieve[j] = False
    return [i for i in range(n+1, 2*n+1) if sieve[i] == True]

while True:
    n = int(input())
    if n == 0:break
    print(len(prime_list(n)))

