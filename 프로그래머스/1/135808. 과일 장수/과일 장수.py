def solution(k, m, score):
    answer = 0
    result = 0
    score.sort(reverse=True)
    
    for i in range(0, len(score), m):
        result = score[i:i+m]

        if len(result) == m:
            answer += (result[-1] * m)

    return answer