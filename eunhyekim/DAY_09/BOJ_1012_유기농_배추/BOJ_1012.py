from collections import deque
import sys

input = sys.stdin.readline

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(sy, sx):
    queue = deque()
    queue.append((sy, sx))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx]:
                queue.append((ny, nx))
                graph[ny][nx] = 0

    return 1

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for sy in range(N):
        for sx in range(M):
            if graph[sy][sx]:
                cnt += bfs(sy, sx)
    print(cnt)
    # print(*graph, sep="\n")
