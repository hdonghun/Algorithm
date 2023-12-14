def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        word = ''
        a = ''
        for b in i:
            word += b # word에 한 글자씩 추가
            if word != a and word in baby: # word가 중복되지 않고 baby안에 있다면
                a = word
                word = ''
        if not word:
            answer += 1
    return answer