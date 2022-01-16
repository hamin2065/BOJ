# https://www.acmicpc.net/problem/5430
# AC
import sys
from collections import deque

def AC(func, ls):
    rotate = 0
    try:
        if ''in ls and 'D' in func:return "error"
        for i in range(len(func)):
            if func[i] == "R":
                rotate += 1
            else:
                if rotate%2 == 1:
                    ls.pop()
                else:
                    ls.popleft()
        if rotate %2 == 1:return list(reversed(ls))
        else:return list(ls)
    except:
        return "error"
        


n = int(input())

for i in range(n):
    try:
        func = list(sys.stdin.readline().strip())
        num = int(sys.stdin.readline().strip())
        ls = deque(sys.stdin.readline().strip()[1:-1].split(","))
        result = AC(func, ls)
        if result == "error":print(result)
        else:print("["+",".join(result)+"]")
    except:
        print("error")