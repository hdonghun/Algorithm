def solution(a, d, included):
    answer = a # 초기 값 세팅
    result = 0 # 나중에 True인 것 들만 받기 위해
    for i in range(len(included)):
        answer += d
        print('answer', answer)
        if included[i] == True:
            result += answer-d
        print('result', result)
  
#     if included[0] == True:
#             result += a
            
    return result