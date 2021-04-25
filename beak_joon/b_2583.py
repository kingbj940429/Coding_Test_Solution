''' 2583번 영역 구하기 '''
from collections import deque
#높이 M, 너비 N, 직사각형 갯수 K
M, N, K = map(int,input().split())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

graph = [[0]*(N) for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())

    for i in range(x1, x2):
        for j in range(y1,y2):
            graph[j][i] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

result = []
def bfs(x,y):
    queue = deque([])    
    queue.append([x,y])
    graph[x][y] = 1
    c = 1

    while queue : 
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1 :
                continue
            else:
                graph[nx][ny] = 1
                c += 1
                queue.append([nx,ny])
    result.append(c)

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            bfs(i,j)

print(len(result))
result.sort()
for i in result:
    print(i,end=" ")


    