# 이것이 취업을 위한 코딩 테스트다 p.96
# 숫자 카드 게임

# N : 행, M : 열
N, M = map(int, input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int, input().split())))
    arr[i].sort()

curr = arr[i][0] 
for i in range(1,N):
    if curr < arr[i][0] : curr = arr[i][0]
print(curr)