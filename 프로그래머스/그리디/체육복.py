def solution(n, lost, reserve):
    answer = n-len(lost)
    lost.sort(reverse = True)
    reserve.sort(reverse = True)
    i = 0;j = 0
    while True :
        if i == len(lost) or j == len(reserve) : break
        if lost[i] <= reserve[j] : 
            answer += 1
            i += 1;j += 1
        else : 
            i += 1
    return answer


n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
print(solution(n,lost,reserve))