# 손익분기점
# https://www.acmicpc.net/problem/1712

a,b,c = map(int, input().split())
# 순이익 
p = c-b

n = 1
if p <= 0:print(-1)
else:
    n += a //p
    print(n)