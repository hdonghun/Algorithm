from collections import deque
def solution(maps):
    
    col = len(maps)
    row = len(maps[0])
    
    def dfs(a,b):
        queue = deque()
        queue.append([a,b])
        dx = [-1,1,0,0] 
        dy = [0,0,-1,1]
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <0 or ny <0 or nx >= col or ny >= row:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append([nx,ny])
        if maps[col-1][row-1] == 1:
            return -1
        else:
            return maps[col-1][row-1]
    answer = dfs(0,0)
    return answer