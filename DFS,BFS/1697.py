# https://www.acmicpc.net/problem/1697
# 숨바꼭질

from collections import deque

n, k = map(int, input().split())
q = deque([n])
arr = [0] * 100001
while True : 
    m = q.popleft()
    if m == k : 
        print(arr[m])
        break
    for i in (m-1,m+1,m*2) : 
        # 이동된 위치가 지정된 범위내여야 하고 
        # arr[i] != 0이면 이미 값이 있다는 뜻으로 최솟값을 구하는게 목표기 때문에 할 필요 X
        if 0 <= i <= 100000 and arr[i] == 0 : 
            arr[i] = arr[m] + 1
            q.append(i)