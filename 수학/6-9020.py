# 골드바흐의 추측
# https://www.acmicpc.net/problem/9020
import math
def gold_prime(k):
    sieve = [True] * k

    for i in range(2, int(math.sqrt(k)) + 1):
        if sieve[i] == True:
            for j in range(2*i, k, i): 
                sieve[j] = False

    prime = [i for i in range(2, k) if sieve[i] == True]
    a = k
    for i in range(len(prime)):
        x = k - prime[i]
        if x in prime:
            if abs(prime[i]-x)<a:
                a = abs(prime[i]-x)
                b = (prime[i],x)
    return min(b[0],b[1]),max(b[0],b[1])

n = int(input())
for _ in range(n):
    result = gold_prime(int(input()))
    print(result[0],result[1])