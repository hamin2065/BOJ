# https://www.acmicpc.net/problem/17218
# 비밀번호 만들기

a = input()
b = input()

DP = [["" for _ in range(len(b))] for _ in range(len(a))]

# 초기값 설정
check = False
for i in range(len(a)) : 
    if a[i] == b[0] or check : 
        DP[i][0] = b[0]
        check = True
        
check = False
for i in range(len(b)) : 
    if b[i] == a[0] or check : 
        DP[0][i] = a[0]
        check = True

for i in range(1,len(a)) : 
    for j in range(1,len(b)) :
        if a[i] == b[j] : 
            DP[i][j] = DP[i-1][j-1]+a[i]
        else : 
            if len(DP[i-1][j]) > len(DP[i][j-1]) :
                DP[i][j] = DP[i-1][j]
            else : 
                DP[i][j] = DP[i][j-1]
            
print(DP[len(a)-1][len(b)-1])