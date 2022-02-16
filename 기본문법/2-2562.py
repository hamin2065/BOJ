# 최댓값
# https://www.acmicpc.net/problem/2562

num_list=[]
for _ in range(9):
    a = int(input())
    num_list.append(a)

max_val = num_list[0]
max_idx = 0
for i,j in enumerate(num_list):
    if j > max_val:
        max_val = j
        max_idx = i
print(max_val)
print(max_idx+1)

# for문 사용하지 않고 내장함수 사용가능
#print(max(num_list))
#print(num_list.index(max(num_list))+1)