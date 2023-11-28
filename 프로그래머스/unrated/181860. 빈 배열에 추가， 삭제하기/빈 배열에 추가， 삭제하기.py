def solution(arr, flag):
    X = []
    # true라면 X의 뒤에 arr[i]를 arr[i] × 2 번 추가
    # false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return
    for i in range(len(arr)):
        if flag[i] == True:
            X += ([arr[i]]*int(arr[i])*2)
        else:
            X = X[:-arr[i]]
            
        
    return X