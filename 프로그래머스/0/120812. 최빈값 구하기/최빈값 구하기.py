def solution(array):
    from collections import Counter

    # 1. 배열에서 각 숫자의 등장 횟수를 센다
    counter = Counter(array)

    # 2. 등장 횟수 중 가장 큰 값을 구한다 (최빈값의 빈도수)
    max_freq = max(counter.values())

    # 3. 가장 많이 등장한 숫자(최빈값 후보)를 수동으로 찾는다
    most_common = []
    for k, v in counter.items():
        if v == max_freq:
            most_common.append(k)

    # 4. 최빈값이 여러 개이면 -1 반환, 아니면 그 값을 반환
    if len(most_common) > 1:
        return -1
    else:
        return most_common[0]
