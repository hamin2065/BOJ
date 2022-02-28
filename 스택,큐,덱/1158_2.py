from collections import deque

n,k = map(int, input().split())

num = deque([i+1 for i in range(n)])

st = []
i = 1
while len(st) != n : 
    if i%k == 0 : 
        st.append(str(num.popleft()))
    else :
        num.append(num.popleft())
    i += 1
print("<"+", ".join(st)+">")