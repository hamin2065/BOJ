def solution(answers):
    res_1 = [i+1 for i in range(5)]
    res_2 = [2,1,2,3,2,4,2,5]
    res_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [[0,1],[0,2],[0,3]]
    for i in range(len(answers)) : 
        if answers[i] == res_1[i%5] : 
            score[0][0] += 1
        if answers[i] == res_2[i%8] : 
            score[1][0] += 1
        if answers[i] == res_3[i%10] : 
            score[2][0] += 1
    score.sort(reverse=True)
    answer = [score[0][1]]
    for i in range(1,3) : 
        if score[i][0] == score[0][0] : 
            answer.append(score[i][1])
    return sorted(answer)