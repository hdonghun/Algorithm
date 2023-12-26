def solution(s):
    p_count=0
    y_count=0
    s = s.lower()
    
    for i in s:
        if i == 'p':
            p_count+=1
        elif i == 'y':
            y_count+=1
            
    if y_count == p_count:
        return True
    else:
        return False
            