# https://www.acmicpc.net/problem/9012
# 괄호

def VPS(arr):
    st = []
    for i in range(len(arr)):
        if arr[i] == '(':
            st.append(arr[i])
        else: 
            if len(st) > 0:
                st.pop()
            else:return "NO"
    if len(st) != 0:return "NO"
    else:return "YES"

n = int(input())
for i in range(n):
    print(VPS(list(input())))