''' 2606번 바이러스 '''
from collections import deque

def get_list(com_cnt, pairs):
    graph = [[] for _ in range(com_cnt+1)]
    
    for _ in range(pairs):
        n, m =map(int,input().split())
        graph[n].append(m)
        graph[m].append(n)

    return graph

def bfs(graph, visited):
    queue = deque([1])
    visited[1] = True
    cnt = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt

def dfs(graph,v,visited , dfs_cnt):
    visited[v] = True
    
    for i in graph[v]:
        if visited[i] == False:
            dfs_cnt+=1
            dfs_cnt = dfs(graph,i,visited, dfs_cnt)

    return dfs_cnt

if __name__ == "__main__":
    com_cnt = int(input())
    pairs = int(input())
    #방문 체크
    visited = [False] * (com_cnt + 1)

    # 정렬 리스트
    graph = []
    graph = get_list(com_cnt, pairs)
    print(bfs(graph, visited))
    #print(dfs(graph,1,visited, 0))
    

    

