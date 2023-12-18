def solution(arr, flag):

    b=[]
    # arr=[3,2,4,1,3]
    # flag=[True,False,True,False,False]

    for i in range(len(flag)):
        if flag[i]:
            for _ in range(arr[i]*2):
                b.append(arr[i])
        else:
            for _ in range(arr[i]):
                b.pop()
    return b