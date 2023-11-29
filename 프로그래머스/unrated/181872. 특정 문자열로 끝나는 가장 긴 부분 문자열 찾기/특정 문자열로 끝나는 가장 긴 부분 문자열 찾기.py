def solution(myString, pat):
    answer = ''
    
    for i in range(len(myString)):
        if myString[i] in pat:
            answer = myString[:i+1]
    
    
    return answer