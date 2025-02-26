from collections import deque


def solution(maps):
    answer = 0
    col, row = len(maps), len(maps[0])
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]
    
    def bfs(start, end):
        q = deque()
        q.append(start)
        visited = [[0]*row for _ in range(col)]
        
        while q:
            x, y = q.popleft()
            
            for k in range(4):
                xi, xj = x + di[k], y + dj[k]
                
                if 0 <= xi < col and 0 <= xj < row and not visited[xi][xj] and maps[xi][xj] != 'X':
                    q.append((xi, xj))
                    visited[xi][xj] = visited[x][y] + 1
                    
        return visited[end[0]][end[1]]
    
    for i in range(col):
        for j in range(row):
            if maps[i][j] == 'S' : start = (i, j)
            elif maps[i][j] == 'L' : lever = (i, j)
            elif maps[i][j] == 'E' : exit = (i, j)
            
            
    distance1 = bfs(start, lever)
    distance2 = bfs(lever, exit)
    
    return distance1 + distance2 if distance1 and distance2 else -1