# https://www.acmicpc.net/problem/2920
# 음계

arr = list(map(int, input().split()))
def solve() : 
    for i in range(1,8) : 
        if abs(arr[i-1]-arr[i]) != 1 : 
            return False
    return True

if solve() == False : 
    print("mixed")
else :
    if arr[0] < arr[1] : 
        print("ascending")
    else : 
        print("descending")