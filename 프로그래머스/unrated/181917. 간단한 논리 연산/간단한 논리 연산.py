def solution(x1, x2, x3, x4):
    answer = False
    print(x2+x3)
    if(x1+x2) and (x3+x4) >=1: # and이기 때문에, 무조건 하나는 True가 존재 하면.
        answer = True
    elif(x1+x2) or (x3+x4) == 0:
        answer = False
    elif(x1+x2) and (x3+x4) == 0:
        answer = False
    
    return answer