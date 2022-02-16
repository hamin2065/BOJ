# 더하기 사이클
# https://www.acmicpc.net/problem/1110


n = int(input())
b = n
count =0
while True:
    a = (b//10)+(b%10)
    b = (a%10) + 10*(b%10)
    count += 1
    if b == n: break
print(count)

