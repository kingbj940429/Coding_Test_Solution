''' 11650번 좌표 정렬하기 '''

N = int(input())

graph = []
for _ in range(N):
	graph.append(list(map(int, input().split())))

graph.sort(key=lambda x : (x[0],x[1]))

for i in range(len(graph)):
	print(graph[i][0], graph[i][1])