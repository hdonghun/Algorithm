def solution(k, score):
    answer = []
    result = []
    
    for i in range(len(score)):
        result.append(score[i])
        result = sorted(result)
        if k <= i:
            result == result.pop(0)
        answer.append(result[0])
    
    return answer