from collections import deque
N, M = map(int, input().split())
graph = [list(map(int,list(input()))) for _ in range(N)]
# print(*graph, sep="\n")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

queue = deque([(0, 0)])

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and graph[ny][nx]==1:
            graph[ny][nx] += graph[y][x]
            queue.append((ny, nx))
    # print(*graph, sep="\n")
    # print("----------------------------------")

print(graph[N-1][M-1])