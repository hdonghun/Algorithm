def solution(n, slicer, num_list):
    answer = []
    
    a = slicer[0]
    b = slicer[1]
    c = slicer[2]
    
    for i in range(len(num_list)):
        if n == 1:
            answer = num_list[0:b+1]
        elif n == 2:
            answer = num_list[a:]
        elif n == 3:
            answer = num_list[a:b+1]
        elif n == 4:
            answer = num_list[a:b+1:c]
        
    return answer