''' 11724번 연결 요소의 개수 '''
from collections import deque
import sys
input = sys.stdin.readline
# 정점의 갯수와 간선의 갯수 받기
N, M = map(int,input().split())

# 방문기록
visited =[False] * (N+1)

# 간선의 양끝점
graph = [[] for _ in range(N+1)]

for _ in range(M):
    i,j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# bfs
def bfs(v):
    queue = deque([])
    queue.append(v)

    while queue :
        k = queue.popleft()

        for i in graph[k]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

cnt = 0
for i in range(1, len(visited)):
    if visited[i] == False:
        bfs(i)
        cnt += 1

print(cnt)




