def solution(babbling):
    answer = 0
    result = ["aya", "ye", "woo", "ma" ]
    for i in babbling:
        if '' in i.split('aya'):
            print("i.split('aya')", i.split('aya'))
            answer += 1
        elif '' in i.split('ye'):
            print("i.split('ye')", i.split('ye'))
            answer += 1
        elif '' in i.split('woo'):
            print("i.split('woo')", i.split('woo'))
            answer += 1
        elif '' in i.split('ma'):
            print("i.split('ma')", i.split('ma'))
            answer += 1
    
    return answer