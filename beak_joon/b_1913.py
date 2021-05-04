''' 1913번 달팽이 '''
# N by N
N = int(input())
# 찾은 값
M = int(input())

graph = [ [0] * N for _ in range(N)]

#방향
direct = 1
# 1의 위치
dx = (N-1) // 2
dy = (N-1) // 2
# 반복할 횟수
cnt = 1
# 값
value = 1
graph[dx][dy] = 1

while N*N != value :
    if direct == 1:
        for i in range(cnt):
            value += 1
            dx -= 1
            dy += 0
            graph[dx][dy] = value
            if value == N*N :
                break
        direct = 2
    elif direct == 2:
        for i in range(cnt):
            value += 1
            dx += 0
            dy += 1
            graph[dx][dy] = value
        direct = 3
        cnt += 1
    elif direct == 3:
        for i in range(cnt):
            value += 1
            dx += 1
            dy += 0
            graph[dx][dy] = value
        direct = 4
    elif direct == 4:
        for i in range(cnt):
            value += 1
            dx += 0
            dy -= 1
            graph[dx][dy] = value
        direct = 1
        cnt += 1

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=" ")
        if M == graph[i][j] :
            find_i = i
            find_j = j 
    print()
print(find_i+1, find_j+1)