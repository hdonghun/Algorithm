def solution(want, number, discount):
    answer = 0
    len_number = sum(number)  # number 리스트의 총합을 구함
    
    for i in range(len(discount) - len_number + 1):  # 인덱스 범위를 조정
        arr = discount[i:i + len_number]  # discount 리스트에서 적절한 범위를 선택
        count = [0] * len(want)  # 각 원소의 출현 횟수를 저장할 리스트 초기화

        for item in arr:
            if item in want:
                count[want.index(item)] += 1

        if count == number:  # 출현 횟수가 일치하는지 확인
            answer += 1

    return answer