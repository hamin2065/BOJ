from collections import deque
from sys import stdin

deq = deque([])

n = int(input())

for i in range(n) : 
    c = stdin.readline().strip().split()
    if c[0] == "push" : 
        deq.append(int(c[1]))
    elif c[0] == "pop" :
        print(deq.popleft() if deq else -1)
    elif c[0] == "size" : 
        print(len(deq))
    elif c[0] == "empty" : 
        print(0 if deq else 1)
    elif c[0] == "front" : 
        print(deq[0] if deq else -1)
    else : 
        print(deq[-1] if deq else -1)
        