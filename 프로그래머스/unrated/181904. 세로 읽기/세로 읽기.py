def solution(my_string, m, c):
    answer = ''
    for i in range(0,len(my_string)):
        answer += my_string[i]
    answer = answer[c-1::m]
    print(answer)
            
    return answer