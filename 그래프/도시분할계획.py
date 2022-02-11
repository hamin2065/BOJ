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
        
v, e = map(int, input().split())
parent = [i for i in range(v+1)]

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보를 입력받기
for _ in range(e) : 
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

# 간선을 하나씩 확인
for edge in edges : 
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b) : 
        union_parent(parent, a, b)
        result += cost
        last = cost # 제일 큰 cost는 제일 마지막에 들어오기 때문에 last에는 최대간선비용이 들어가게됨
        
print(result - last)