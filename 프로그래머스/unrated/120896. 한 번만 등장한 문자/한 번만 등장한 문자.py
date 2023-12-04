def solution(s):
    answer = ''

    for i in range(len(s)):
        count = 0
        for j in range(0,len(s)):
            if s[i] == s[j]:
                count += 1
        if count == 1:
            answer += s[i]
    answer = sorted(answer)
    answer = ''.join(answer)
    return answer