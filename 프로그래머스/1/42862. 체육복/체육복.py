def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    
    for i in range(1, n+1):
        if i in lost and i in reserve: # 여분의 체육복을 가진 학생이 도난당한 경우
            lost.remove(i)
            reserve.remove(i)
            
        elif i in reserve: # 여분의 체육복을 가진 학생이 도난당하지 않았을 경우
            if i-1 in lost:
                lost.remove(i-1)
                reserve.remove(i)
            elif i+1 in lost:
                if i+1 in reserve:
                    continue
                lost.remove(i+1)   
                reserve.remove(i)
                
    answer = n - len(lost)
    
    return answer