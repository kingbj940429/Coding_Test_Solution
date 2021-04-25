'''1012 유기농 배추 '''
import sys
sys.setrecursionlimit(10**9)

def init_graph(graph, K):
    for i in range(K):
        m, n = map(int,input().split())
        graph[n][m] = 1

    return graph

def dfs(x,y):
    
    if x<0 or x>=N or y<0 or y>=M:
        return False
    
    #배추가 심어져있을때
    if graph[x][y] == 1 :
        graph[x][y] = 0
        dfs(x-1,y)#상
        dfs(x+1,y)#하
        dfs(x,y-1)#좌
        dfs(x,y+1)#우
        return True
    #배추가 안심어져있을때
    return False
    
T = int(input())

for _ in range(T):
    #가로, 세로, 배추의 수
    M,N,K = map(int,input().split())
    cnt = 0
    #배추밭 초기화
    graph = [[0]*M for _ in range(N)]
    graph = init_graph(graph, K)
    
    for i in range(N):
        for j in range(M):
            if dfs(i,j) == True:
                cnt += 1
    print(cnt)
    

