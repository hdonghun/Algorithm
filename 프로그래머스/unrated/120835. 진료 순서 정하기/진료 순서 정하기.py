def solution(emergency):
    temp = sorted(emergency, reverse = True)
    # temp에는 [76,24,3]
    # 그럼 기존 emergency를, [3,76,24] for in 으로 돌려서
    # temp.index(i) 로 하면
    # 원소 3에 대한, 순서를 정한 인덱스 값(temp에 대해)을 return 해주면
    # 원소 3가, 몇 번째 인덱스 인지 알 수 있다.
    answer = []
    
    for i in emergency:
        answer.append(temp.index(i)+1) # +1을 해주는 이유는 인덱스가 1부터 시작하는 것 처럼, 문제가 나와서, 인덱스 0이 인덱스 1임
        
    return answer