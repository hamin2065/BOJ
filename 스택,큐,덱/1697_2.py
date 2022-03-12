from collections import deque

n,k = map(int, input().split())

que = deque([n])

arr = [0]*100001

while True : 
    # 수빈이가 서있는 자리
    m = que.popleft()
    if m == k : # 동생을 찾았다면
        print(arr[m])
        break
    for i in (m-1,m+1,m*2) : # 수빈이가 이동할 수 있는 자리
        # 범위 내. arr[i] != 0이면 이미 값이 있다는 뜻 -> 이미 있는 값이 최솟값
        if 0 <= i <= 100000 and arr[i] == 0 : 
            arr[i] = arr[m] + 1
            que.append(i)