# 이것이 취업을 위한 코딩 테스트다 p.197
# 부품 찾기

def binary_search(store, target):
    start = 0;end = n-1
    while start <= end : 
        mid = (start+end)//2
        if store[mid] == target :
            return "YES"
        elif store[mid] < target : 
            start = mid + 1
        else : 
            end = mid - 1
    return "NO"


n = int(input())
store = list(map(int, input().split()))
m = int(input())
customer = list(map(int, input().split()))
store.sort()
for i in range(m) : 
    print(binary_search(store, customer[i]))
    