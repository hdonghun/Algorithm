def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    
    # 1. 여분의 체육복을 가진 학생이 도난당한 경우를 처리
    new_lost = [l for l in lost if l not in reserve]
    new_reserve = [r for r in reserve if r not in lost]
    
    # 2. 남은 여분의 체육복을 가진 학생들이 도난당한 경우를 처리
    for r in new_reserve:
        if r - 1 in new_lost:
            new_lost.remove(r - 1)
        elif r + 1 in new_lost:
            new_lost.remove(r + 1)
    
    # 3. 남은 여분의 체육복을 가진 학생들이 도난당하지 않은 경우를 처리
    answer = n - len(new_lost)
    
    return answer