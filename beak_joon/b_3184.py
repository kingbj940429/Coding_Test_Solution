''' 3184번 양 '''
from collections import deque

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(m, n):
    queue = deque([])
    queue.append([m,n])
    
    wolf = 0
    sheep = 0

    while queue : 
        x, y = queue.popleft()

        if graph[x][y] == 'v':
            wolf += 1
            graph[x][y] = '#'
        elif graph[x][y] == 'o':
            sheep += 1
            graph[x][y] = '#'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C :
                continue
            if graph[nx][ny] == '#':
                continue
            #늑대일때
            if graph[nx][ny] == '.':
                graph[nx][ny] = '#'
                queue.append([nx, ny])
            elif graph[nx][ny] == 'v':
                wolf += 1
                graph[nx][ny] = '#'
                queue.append([nx, ny])
            elif graph[nx][ny] == 'o':
                sheep += 1
                graph[nx][ny] = '#'
                queue.append([nx, ny])
    if wolf < sheep :
        return [sheep, 0]
    else:
        return [0, wolf]
            
# 행과 열을 받는다
R, C = map(int,input().split())

# 마당 입력 받기
graph = [list(input()) for _ in range(R)]

wolf = 0
sheep = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == '.' or graph[i][j] == 'o' or graph[i][j] == 'v':
            temp1, temp2 = map(int,bfs(i, j))
            sheep += temp1
            wolf += temp2
print(sheep, wolf)
