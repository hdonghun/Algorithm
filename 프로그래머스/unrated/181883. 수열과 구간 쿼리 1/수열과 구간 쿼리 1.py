def solution(arr, queries):
    answer = arr
    
    for query in queries:
        start, end = query
        for i in range(start, end + 1):
            answer[i] += 1

    return answer