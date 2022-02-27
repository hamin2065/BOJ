from collections import deque
def solution(n, computers):
    answer = 0
    for i in range(n) : 
        if BFS(i,n,computers) : answer += 1
    return answer

def BFS(num,n,computers) :
    if computers[num][num] != 1 : return False
    computers[num][num] = 0
    d = deque()
    d.append(num)
    while d : 
        number = d.popleft()
        # 방문처리
        computers[number][number] = 0
        # 각 컴퓨터에 대해 연결된게 있는지 다 검사
        for i in range(n) : 
            if computers[number][i] == 1 : 
                computers[number][i] = 0
                computers[i][i] = 0
                computers[i][number] = 0
                d.append(i)
    return True