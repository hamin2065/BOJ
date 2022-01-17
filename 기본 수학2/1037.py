# https://www.acmicpc.net/problem/1037
# 약수

n = int(input())

arr = list(map(int, input().split()))
arr.sort()
if n%2 == 1:print(arr[len(arr)//2]**2)
else:print(arr[0]*arr[-1])