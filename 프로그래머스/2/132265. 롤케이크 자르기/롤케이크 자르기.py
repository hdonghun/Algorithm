def solution(topping):
    answer = 0
    prefix_types = {}  # 각 위치에서의 접두사 토핑 종류 수를 저장할 딕셔너리
    suffix_types = {}  # 각 위치에서의 접미사 토핑 종류 수를 저장할 딕셔너리
    
    # 왼쪽에서 오른쪽으로 이동하면서 접두사 토핑 종류 수 계산
    prefix_set = set()
    for i in range(len(topping)):
        prefix_set.add(topping[i])
        prefix_types[i] = len(prefix_set)
    
    # 오른쪽에서 왼쪽으로 이동하면서 접미사 토핑 종류 수 계산
    suffix_set = set()
    for i in range(len(topping) - 1, -1, -1):
        suffix_set.add(topping[i])
        suffix_types[i] = len(suffix_set)
    
    # 각 위치에서의 접두사와 접미사 토핑 종류 수가 같은 경우 공평하게 자른 경우이므로 answer 증가
    for i in range(len(topping) - 1):
        if prefix_types[i] == suffix_types[i + 1]:
            answer += 1
            
    return answer