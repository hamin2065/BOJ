# 소수
# https://www.acmicpc.net/problem/2581
import math
def prime(n):
    if n <= 1:return True
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:return True
    return False
a = int(input())
b = int(input())
arr = []
for i in range(a,b+1):
    if prime(i) == False:arr.append(i)
if len(arr) == 0:print(-1)
else:
    print(sum(arr))
    print(arr[0])