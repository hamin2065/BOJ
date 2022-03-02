n = int(input())

tri = [list(map(int, input().split())) for _ in range(n)]

DP = [[0 for _ in range(n)] for _ in range(n)]

DP[n-1] = tri[n-1]

for i in range(n-2,-1,-1) : 
    for j in range(len(tri[i])) : 
        DP[i][j] = max(DP[i+1][j]+tri[i][j], DP[i+1][j+1]+tri[i][j])
        
print(DP[0][0])