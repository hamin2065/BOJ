# https://www.acmicpc.net/problem/1158
# 요세푸스 문제
from collections import deque
n,k = map(int, input().split())
que = deque([i+1 for i in range(n)])
result = ""
i = 1
while len(que) != 0:
    if i % k == 0:
        result += str(que.popleft())
        result += ", "
    else:
        que.append(que.popleft())
    i += 1
print("<"+result[:-2]+">")