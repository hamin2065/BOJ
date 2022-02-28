from collections import deque
num = int(input())

for _ in range(num) : 
    n,m = map(int, input().split())
    _li = list(map(int, input().split()))
    li = deque([])
    for i in range(n) : li.append((_li[i],i))
    count = 0
    while li :
        k = max(li)[0]
        if k > li[0][0] : 
            li.append(li.popleft())
        else : 
            if li[0][1] == m :
                li.popleft()
                count += 1
                print(count)
                break
            else : 
                li.popleft()
                count += 1
            
        