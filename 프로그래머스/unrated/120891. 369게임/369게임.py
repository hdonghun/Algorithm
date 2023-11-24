def solution(order):
    answer = 0
    order=str(order)
    order = list(order)
    print(order)
    for i in range(len(order)):
        if order[i] in ('3','6','9'):
            answer+=1

    return answer