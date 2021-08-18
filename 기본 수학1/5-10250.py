# ACM 호텔
# https://www.acmicpc.net/problem/10250
import math
def room(H,N):
    Y = N % H # 층
    if Y == 0:Y = H
    X = math.ceil(N/H)
    return 100*Y+X

T = int(input())
for _ in range(T):
    H,W,N = map(int, input().split())
    result = room(H,N)
    print(result)