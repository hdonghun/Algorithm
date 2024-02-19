def solution(n, left, right):
    answer = []

    arr = []

    for i in range(left, right + 1):
        row = i // n
        col = i % n
        # 해당 요소의 값은 (행 번호 + 1)과 (열 번호 + 1) 중에서 큰 값으로 설정
        arr.append(max(row + 1, col + 1))

    return arr