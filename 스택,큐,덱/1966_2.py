from sys import stdin
from collections import deque
num = int(input())

def AC(f,arr) : 
    rot = 0
    try : 
        if '' in arr and 'D' in f : 
            return "error"
        for c in f : 
            if c == "D" : 
                if rot%2 == 0 : 
                    arr.popleft()
                elif rot % 2 != 0 : 
                    arr.pop()
            elif c == "R" : 
                rot += 1
        if rot % 2 == 1 : 
            return list(reversed(arr))
        else : 
            return list(arr)
    except : 
        return "error"

for _ in range(num) : 
    try : 
        f = list(input())
        n = int(input())
        arr = deque(stdin.readline().strip()[1:-1].split(','))
        result = AC(f,arr)
        if result == "error" : print(result)
        else : 
            print("["+",".join(result)+"]")
    except : 
        print("error")