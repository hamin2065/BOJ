# https://www.acmicpc.net/problem/10845
# 큐

from collections import deque
import sys
deq = deque()
def push(a):
    deq.append(a)
def front():
    if len(deq) == 0:
        print(-1)
        return
    print(deq[0])
def back():
    if len(deq) == 0:
        print(-1)
        return
    print(deq[-1])
def size():
    print(len(deq))
def pop():
    if len(deq) == 0:
        print(-1)
        return
    print(deq.popleft())
def empty():
    if len(deq):print(0)
    else:print(1)
    

n = int(input())
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        push(command[1])
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "front":
        front()
    else:
        back()