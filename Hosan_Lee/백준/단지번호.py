import sys #stdin 사용하기 위해서 import


def dfs_recursive(x, y) :
    visited[x][y] = 1
    global nums
    if graph[x][y] == 1 :
        nums += 1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1 :
                dfs_recursive(nx, ny)

N = int(input())
graph = []
nums = 0
visited = [[0]*N for _ in range(N)]
numlist= []
for i in range(N) :
    graph.append(list(map(int, input())))
#입력


dx = [1, -1, 0, 0] #상하좌우
dy = [0, 0, 1, -1]

for a in range(N):
    for b in range(N) :
        if graph[a][b] == 1 and visited[a][b] == 0 :
            dfs_recursive(a, b)
            numlist.append(nums)
            nums = 0

print(len(numlist))
for n in sorted(numlist) :
    print(n)
