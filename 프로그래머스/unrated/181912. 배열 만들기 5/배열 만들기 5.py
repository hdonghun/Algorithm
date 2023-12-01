def solution(intStrs, k, s, l):
    answer = []
    
    for i in range(len(intStrs)):
        tmp = ''
        for j in range(s, s+l):
            tmp += intStrs[i][j]
            if int(tmp) > k:
                tmp = int(tmp)
                answer.append(tmp)
    return answer