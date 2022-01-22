# https://www.acmicpc.net/problem/1182
# 부분수열의 합

n,s = map(int, input().split())
nums = list(map(int, input().split()))
result = 0
def solve(i,sub_sum):
    global result
    
    if i >= n:return
    
    sub_sum += nums[i]
    if sub_sum == s:
        result += 1
    
    solve(i+1, sub_sum)
    solve(i+1, sub_sum-nums[i])
    
solve(0,0)
print(result)