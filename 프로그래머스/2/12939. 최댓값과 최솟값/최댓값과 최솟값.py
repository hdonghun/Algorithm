def solution(s):
    answer = ''
    result = []
    
    s = s.split(' ')
    
    for i in range(len(s)):
        result.append(int(s[i]))
    
    s_max = max(result)
    s_min = min(result)
    answer = str(s_min),str(s_max)
    f'{s_min} {s_max}'
    return f'{s_min} {s_max}'