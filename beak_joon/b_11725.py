''' 11725번 트리의 부모 찾기 '''
from collections import deque
import sys
input = sys.stdin.readline
#노드의 갯수
N = int(input())

graph =[]
visited = [False] * (N+1)
for _ in range(N+1):
    graph.append([])

for _ in range(N-1):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
ans = {}
def bfs(graph, visited):
    queue = deque([])
    queue.append(1)
    visited[1] = True

    while queue : 
        parent = queue.popleft()
        
        for i in graph[parent]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                ans[i] = parent
bfs(graph, visited)
for i in range(2,N+1):
    print(ans.get(i))

