def solution(arr):
    answer = []
    n=1
    while 2**n <len(arr):
        n+=1

    if len(arr)== n:
        return arr
    
    else:
        while len(arr)!=2**n:
            arr.append(0)
    return arr