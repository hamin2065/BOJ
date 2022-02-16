# https://www.acmicpc.net/problem/2609
# 최대공약수와 최소공배수

from math import gcd

x,y = map(int, input().split())
print(gcd(x,y))
print(x*y//gcd(x,y))