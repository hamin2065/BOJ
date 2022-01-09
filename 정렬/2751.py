# https://www.acmicpc.net/problem/2751
# 수 정렬하기 2
import sys
input = sys.stdin.readline
n = int(input())
arr=[]
for i in range(n):arr.append(int(input()))
arr.sort()
for i in range(n):print(arr[i])