# 이것이 취업을 위한 코딩테스트다 p.217
# 1로 만들기

x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x+1) : 
    # '+1'이 의미하는 것은 연산을 수행했다는 것. 
    
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0 : 
        d[i] = min(d[i], d[i//2]+1)
    
    # 현재의 수가 3로 나누어 떨어지는 경우
    if i % 3 == 0 : 
        d[i] = min(d[i], d[i//3]+1)
    
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0 : 
        d[i] = min(d[i], d[i//5]+1)

print(d[x])
        
        