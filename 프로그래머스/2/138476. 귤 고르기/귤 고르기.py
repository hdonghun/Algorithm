def solution(k, tangerine):
    count_dict = {}  # 각 숫자의 등장 횟수를 저장할 딕셔너리
    result = []  # 결과 리스트
    count = 1
    
    # 등장 횟수 계산
    for num in tangerine:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # 딕셔너리를 이용하여 결과 리스트 생성
    for num, frequency in count_dict.items():
        result.append([num, frequency])
    
    # 등장 횟수를 기준으로 정렬
    result_sorted = sorted(result, key=lambda x: x[1], reverse=True)
    
    # 인덱스를 이용하여 k를 초과하는 순간의 인덱스를 반환
    for i in range(len(result_sorted)):
        if result_sorted[i][1] >= k:
            return count
        else:
            k -= result_sorted[i][1]
            count += 1