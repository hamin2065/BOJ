# https://www.acmicpc.net/problem/13305
# 주유소

n = int(input())
road_length = list(map(int, input().split()))
liter = list(map(int, input().split()))

curr_li = liter[0]

total = curr_li*road_length[0] # 처음에는 무조건 필요
# 현재 리터 가격이 더 작다면 curr_li의 값을 바꿔준다.
for i in range(1,len(road_length)):
    if liter[i]<=curr_li:
        curr_li = liter[i]
    total += curr_li*road_length[i]
print(total)