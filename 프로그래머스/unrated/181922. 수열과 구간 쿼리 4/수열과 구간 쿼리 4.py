def solution(arr, queries):
    answer = arr

    for a in queries:
        i = a[0]
        j = a[1]
        k = a[2]

        for c in range(i, j+1):
            if c % k == 0:
                answer[c] += 1

    return answer