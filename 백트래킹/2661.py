# https://www.acmicpc.net/problem/2661
# 좋은 수열

n = int(input())

arr = []

def solve(idx) : 
    # 나쁜 수열인 경우
    for i in range(1, idx//2+1) : 
        if arr[-i:] == arr[-2*i:-i] :
            return -1
    if idx == n : 
        for i in range(n) : 
            print(arr[i],end='')
        return 0
    for i in range(1, 4) : 
        arr.append(i)
        # 좋은 수열
        if solve(idx+1) == 0 : 
            return 0
        arr.pop()

solve(0)