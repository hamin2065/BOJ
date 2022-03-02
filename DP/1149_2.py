n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
# arr[i][0] => 빨
# arr[i][1] => 초
# arr[i][2] => 파

DP = [[0 for _ in range(3)] for _ in range(n)]

DP[0] = arr[0]

for i in range(1,n):
    DP[i][0] = min(DP[i-1][1]+arr[i][0],DP[i-1][2]+arr[i][0])
    DP[i][1] = min(DP[i-1][0]+arr[i][1],DP[i-1][2]+arr[i][1])
    DP[i][2] = min(DP[i-1][0]+arr[i][2],DP[i-1][1]+arr[i][2])
    
print(min(DP[n-1]))