# https://www.acmicpc.net/problem/2485
# 가로수
import math
n = int(input())
tree = [int(input()) for _ in range(n)]

gap = []

for i in range(n-1) : 
    gap.append(tree[i+1]-tree[i])

gcd = gap[0]
for i in range(len(gap)) : 
    gcd = math.gcd(gcd, gap[i])
total = 0
for i in range(len(gap)) : 
    total += (gap[i]//gcd-1)
    
print(total)