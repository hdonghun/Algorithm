def solution(n, lost, reserve):
    lost ,reserve = list(set(lost) - set(reserve)) , list(set(reserve) - set(lost))
    for r in reserve:
        f = r - 1
        b = r + 1
        if f in lost:
            lost.remove(f)
        elif b in lost:
            lost.remove(b)
    return n - len(lost)