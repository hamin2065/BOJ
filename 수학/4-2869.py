# 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869
import math
A,B,V = map(int, input().split())
i = 1
V = V-A # 무조건 낮에 끝나니까 마지막 날 낮에 올라가는 만큼 빼고 시작
if V <= 0:print(i)#1일 : 낮에 다 올라가는 경우
else:# 하루보다 더 걸리는 경우
    V /= (A-B)
    i += math.ceil(V)
    print(i)
