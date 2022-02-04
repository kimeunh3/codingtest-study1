import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
field = [ list(map(int, list(input().strip()))) for _ in range(N) ]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cnt_lst = []

def bfs(x, y):
    queue = deque([(x, y)])
    field[y][x] = 0 
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and field[ny][nx]:
                queue.append((nx, ny))
                field[ny][nx] = 0 
    return cnt

for y in range(N):
    for x in range(N):
        if field[y][x]:
            cnt_lst.append(bfs(x, y))

print(len(cnt_lst))
print(*sorted(cnt_lst), sep="\n")