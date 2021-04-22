''' 1260 DFS와 BFS '''
from collections import deque
import sys

input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    dfs_graph.append(v)

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([])
    queue.append(v)
    visited[v] = True
    bfs_graph.append(v)
    while queue:
        k = queue.popleft()

        for i in graph[k]:
            if visited[i] == False:
                queue.append(i)
                bfs_graph.append(i)
                visited[i] = True
    return bfs_graph

N, M, V = map(int, input().split())

dfs_graph = []
bfs_graph = deque([])

graph = [[] for _ in range(10000+1)]
visited = [False] * (N+1)

#graph에 정렬리스트 담기
for _ in range(M):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

#graph 오름차순 정렬
for i  in range(1,M):
    graph[i] = sorted(graph[i])

dfs(graph, V, visited)

#방문 리스트 초기화
visited = [False] * (N+1)
bfs_graph = list(bfs(graph, V, visited))

for data in dfs_graph:
    print(data, end=" ")
print()
for data in bfs_graph:
    print(data, end=" ")
