def solution(land):
    if len(land) == 1:
        return max(*land)
    
    for i in range(1, len(land)):
        for j in range(4):
            now = land[i][j]
            for k in range(4):
                if k == j:
                    continue
                land[i][j] = max(land[i][j], now + land[i-1][k])
                
    return max(land[-1])