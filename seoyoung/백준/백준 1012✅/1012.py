from collections import deque
tc = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny] == 0:
                continue
            queue.append((nx, ny))
            graph[nx][ny] = 0
    return


for i in range(tc):
    answer = 0
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    for i in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1
    print(graph)
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                answer += 1

    print(answer)
