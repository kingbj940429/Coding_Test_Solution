''' 4963번 섬의 개수 '''


from _collections import deque

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    island = [list(map(int, input().split())) for _ in range(h)]

    # 상 우상 우 우하 하 좌하 좌 좌상
    # 8방향 탐색을 위해
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    # 속도가 빠른 디큐를 사용
    q = deque()
    cnt = 0
    for i in range(h):
        for j in range(w):
            # 먼저 육지인 곳을 찾는다.
            if island[i][j] == 1:
                # 육지를 q에 넣어주고
                q.append((i, j))
                # 방문했다는 표시로 값을 2로 바꿔준다.
                island[i][j] = 2

                while q:
                    # 현재 위치를 q에서 꺼내주고
                    cx, cy = q.popleft()
                    # 8방향 탐색을 해준다.
                    for k in range(8):
                        nx = cx + dx[k]
                        ny = cy + dy[k]
                        # 전체 배열 범위 안에 있으면서
                        if 0 <= nx < h and 0 <= ny < w:
                            # 육지이면 값을 2로 바꿔주고 q에 넣어준다.
                            if island[nx][ny] == 1:
                                q.append((nx, ny))
                                island[nx][ny] = 2

                # 이어져 있는 육지를 다 돌았다면 cnt+1
                else:
                    cnt += 1

    print(cnt)