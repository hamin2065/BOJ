n = int(input()) # 모함가
fear = list(map(int, input().split()))

fear.sort(reverse = True)

count = 0
idx = 0
while idx < len(fear) : 
    idx = fear[0]
    count += 1
print(count)