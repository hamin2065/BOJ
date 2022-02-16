# 문자열 반복
# https://www.acmicpc.net/problem/2675

n = int(input())

for i in range(n):
    m,s = map(str, input().split())
    m = int(m)
    s = list(s)
    result = list(map((lambda x:x*m),s))
    print(''.join(result))