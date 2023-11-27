def solution(my_string, indices):
    answer = ''
    
    for i in enumerate (my_string):
        if i[0] not in indices:
            answer+=i[1]
        
    return answer