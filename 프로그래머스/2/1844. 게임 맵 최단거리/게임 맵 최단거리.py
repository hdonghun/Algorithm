from collections import deque

def bfs(maps):
    cnt = 1
    queue = deque()
    max_x = len(maps)
    max_y = len(maps[0])
    queue.append([max_x-1, max_y-1, cnt])
    maps[max_x-1][max_y-1] = 0
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    while queue:
        x, y, cnt = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == 0 and ny == 0:
                return cnt + 1
            if 0 <= nx < max_x and 0 <= ny < max_y:
                if maps[nx][ny] != 0:
                    maps[nx][ny] = 0
                    queue.append([nx, ny, cnt+1])

    return -1

def solution(maps):
    answer = bfs(maps)
    return answer
