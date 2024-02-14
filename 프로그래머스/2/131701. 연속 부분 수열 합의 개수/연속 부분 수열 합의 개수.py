def solution(elements):
    elements_1 = elements * 2  # 리스트를 두 번 이어붙여서 원형 수열을 만듭니다.

    sum_set = set()  # 중복된 값을 제거하기 위한 집합을 생성합니다.

    # 모든 연속 부분 수열의 합을 저장합니다.
    for i in range(len(elements)):
        for j in range(i + 1, i + len(elements) + 1):
            sum_set.add(sum(elements_1[i:j]))  # 부분 수열의 합을 집합에 추가합니다.

    return len(sum_set)  # 집합의 길이가 중복을 제거한 서로 다른 값의 개수입니다.