def solution(board, k):
    answer = 0
    
    for i in range(0, len(board)):
        for j in range(0, len(board)-1):
            if board[i][j] <= k:
                answer+=i
                answer+=j
            
    
    return answer