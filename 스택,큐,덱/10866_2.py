from sys import stdin
from collections import deque

deq = deque([])

n = int(input())

for _ in range(n) : 
    c = stdin.readline().strip().split()
    if c[0] == "push_front" : 
        deq.appendleft(int(c[1]))
    elif c[0] == "push_back" :
        deq.append(int(c[1])) 
    elif c[0] == "pop_front" :
        print(deq.popleft() if deq else -1) 
    elif c[0] == "pop_back" : 
        print(deq.pop() if deq else -1) 
    elif c[0] == "size" : 
        print(len(deq))
    elif c[0] == "empty" : 
        print(0 if deq else 1)
    elif c[0] == "front" : 
        print(deq[0] if deq else -1)
    else : 
        print(deq[-1] if deq else -1)