def solution(arr, queries):    
    for i,j in queries:
        arr[j], arr[i] = arr[i], arr[j]
    
    return arr