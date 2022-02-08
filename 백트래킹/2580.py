# https://www.acmicpc.net/problem/2580
# 스도쿠

s = [list(map(int, input().split())) for _ in range(9)]

# s[i][j] = k가 될 수 있는지 확인
def row(i,j,k) : 
    for o in range(9) : 
        if s[i][o] == k : 
            return False
    return True
    
def col(i,j,k) : 
    for o in range(9) : 
        if s[o][j] == k : 
            return False
    return True
    
def square(i,j,k) : 
    for o in range(3) : 
        for p in range(3) : 
            if s[3*(i//3)+p][3*(j//3)+o] == k : 
                return False
    return True

    
def solve(idx) : 
    if idx == len(check) : 
        for i in range(9) : 
            print(*s[i])
        exit(0)
    x = check[idx][0];y = check[idx][1]
    for k in range(1,10) : 
        if row(x,y,k) == True and col(x,y,k) == True and square(x,y,k) == True : 
            s[x][y] = k
            solve(idx+1)
            s[x][y] = 0


check = []
for i in range(9) : 
        for j in range(9) : 
            if s[i][j] == 0 : 
                check.append((i,j))
solve(0)

