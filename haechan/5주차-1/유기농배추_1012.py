'''백준 유기농 배추 1012번'''
from collections import deque

def get_worms_cnt(graph, sx, sy, n, m):
    global worm_cnt
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]
    dq = deque()
    dq.append((sx, sy))
    if graph[sx][sy] == 1:
        graph[sx][sy] = 0
    
    while dq: # 인접한 밭에 배추가 없을 때까지(인접 값이 모두 0이 될 때까지)
        x, y = dq.popleft()
        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1: 
                graph[nx][ny] = 0; 
                dq.append((nx, ny))
        
    worm_cnt += 1

# ========= 함수 실행 부분 =========
test_case = int(input())
for _ in range(test_case):
    worm_cnt = 0 
    n, m, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1 # 배추의 위치 표시

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1: # 배추가 있는 곳에서부터
                get_worms_cnt(graph, i, j, n, m) # 인접한 밭의 모든 배추를 방문처리(0처리)하고 '지렁이 수 +1'
    print(worm_cnt)