# 이것이 취업을 위한 코딩 테스트다 p.92
# 큰 수의 법칙

N, M, K = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

print(arr[-1]*(M//K)*K+arr[-2]*(M%K))