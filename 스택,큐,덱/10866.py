# https://www.acmicpc.net/problem/10866
# 덱

import sys
from collections import deque
deq = deque()
input = sys.stdin.readline

def push_front(x):
    deq.appendleft(x)
def push_back(x):
    deq.append(x)
def pop_front():
    if len(deq) == 0:return -1
    else:return deq.popleft()
def pop_back():
    if len(deq) == 0:return -1
    else:return deq.pop()
def size():
    return len(deq)
def empty():
    if len(deq) == 0:return 1
    else:return 0
def front():
    if len(deq) == 0:return -1
    return deq[0]
def back():    
    if len(deq) == 0:return -1
    return deq[-1]

n = int(input())
for i in range(n):
    command = input().split()
    if command[0] == "push_front":
        push_front(command[1])
    elif command[0] == "push_back":
        push_back(command[1])
    elif command[0] == "pop_front":
        print(pop_front())
    elif command[0] == "pop_back":
        print(pop_back())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "front":
        print(front())
    else:
        print(back())