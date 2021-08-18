# 분수찾기
# https://www.acmicpc.net/problem/1193

n = int(input())
# a -> 분자, b -> 분모  | a/b

i = 1
while n-i > 0:
    n -= i
    i += 1
# a+b = i-1
# i-1 번째 칸에 있음

if i%2 == 0:
    a = 0;b = i+1
    for _ in range(n):
        a += 1
        b -= 1
else:
    a = i+1;b = 0
    for _ in range(n):
        a -= 1
        b += 1
print(f'{a}/{b}')