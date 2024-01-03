def solution(x):
    result = 0
    x = str(x)
    
    for i in x:
        result += int(i)
        
    if int(x) % result == 0:
        return True
    else:
        return False