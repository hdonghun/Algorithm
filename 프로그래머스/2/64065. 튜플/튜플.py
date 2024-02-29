import re

def solution(s):
    temp = [list(map(int, re.findall(r'\d+',i))) for i in s.split('},{')]
    temp_1 = sorted(temp,key=len)

    result = []
    for i in temp_1:
        for j in range(len(i)):
            if i[j] not in result:
                result.append(i[j])        
    # 하위 리스트의 길이가 가장 짧은 값에서 값이 뭐가 있는지 확인
    # 다음 하위 리스트의 길이가 짧은것을 확인하고, 위에 있는 값을 제외하고 다른 값 확인
    # 계속 진행
    # 모든 하위 리스트에서 뽑은 값을 반환
        
    return result