from collections import deque
def solution(begin, target, words):
    if target not in words : return 0
    visited = [False]*len(words)
    answer = BFS(begin, target, words, visited)
    return answer

def BFS(begin, target, words, visited) : 
    d = deque()
    d.append((begin,0))
    while d : 
        curr, depth = d.popleft()
        if curr == target : 
            return depth
        
        for i in range(len(words)) : 
            if visited[i] == True : continue
            cnt = 0
            for a,b in zip(curr, words[i]) : 
                if a != b : 
                    cnt += 1
            if cnt == 1 : 
                visited[i] = True
                d.append((words[i],depth+1))