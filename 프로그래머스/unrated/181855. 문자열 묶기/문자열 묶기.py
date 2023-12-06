def solution(strArr):
    a = [0]*31
    for x in strArr:
        a[len(x)] += 1
    
    return max(a)