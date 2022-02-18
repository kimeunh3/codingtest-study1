from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input())) for i in range(N)]


def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y]+1


bfs(0, 0)
print(graph[N-1][M-1])
