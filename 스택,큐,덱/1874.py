# https://www.acmicpc.net/problem/1874
# 스택 수열

from sys import stdin
from collections import deque

def sol():
    n = int(input())
    num = deque(range(1, n+1))
    stack = [0]
    cals = []
    for _ in range(n) : 
        a = int(stdin.readline())
        b = len(num)
        if a == stack[-1] : 
            stack.pop()
            cals.append('-')
        else : 
            for _ in range(b) : 
                if num[0] <= a :
                    stack.append(num[0])
                    num.popleft()
                    cals.append('+')
                else :  
                    break
            if a != stack[-1] : 
                print("NO")
                exit()
            else : 
                stack.pop()
                cals.append('-')
    print("\n".join(cals))
sol()