# 이것이 취업을 위한 코딩테스트다 p.298
# 팀 결성

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x) : 
    if parent[x] != x : 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) : 
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b : 
        parent[b] = a
    else : 
        parent[a] = b
        
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

# 각 연산을 하나씩 확인
for i in range(m) : 
    oper, a, b = map(int, input().split())
    # 합집한(union)인 경우
    if oper == 0 : 
        union_parent(parent, a, b)
    # 찾기(find) 연산인 경우
    elif oper == 1 : 
        if find_parent(parent, a) == find_parent(parent, b) : 
            print("YES")
        else : 
            print("NO")