# https://www.acmicpc.net/problem/1966
# 프린터 큐

from collections import deque
import sys

def printer(k,papers):
    index = k # 순서 체크해야되는 문서의 현재 위치
    m = max(papers)
    cnt = 0
    # 자기 자신이 최댓값일 때까지
    while m != papers[index]:
        # 뒤의 문서들 중에 나보다 큰 게 남아있는 경우
        if papers[0] < m :
            papers.append(papers.popleft())
        else: # 현재 있는 문서중 가장 중요도 높은 문서 출력
            papers.popleft()
            m = max(papers)
            cnt += 1
        index -= 1# 현재 문서의 위치는 계속 앞으로 오기 때문에 1씩 줄어든다.
        if index < 0 : # 알아야되는 문서가 맨 뒤로 간 경우
            index = len(papers)-1
    # 자신이 출력될 때까지 
    while papers and index != 0:
        if papers[index] == papers[0]:
            cnt += 1
        else:pass
        papers.popleft()
        index -= 1
    return cnt + 1

num = int(input())

for i in range(num):
    n,k = map(int, input().split())
    papers = deque(map(int, sys.stdin.readline().strip().split()))
    print(printer(k,papers))
