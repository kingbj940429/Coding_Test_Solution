''' 음료수 얼려먹기 '''

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if(x <= -1 or x >= N or y<=-1 or y >= M):
        return False
    if(graph[x][y] == 0):
        graph[x][y] = 1
        dfs(x-1,y)#상
        dfs(x+1,y)#하
        dfs(x,y-1)#좌
        dfs(x,y+1)#우
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if(dfs(i,j) == True):
            result += 1

print(result)