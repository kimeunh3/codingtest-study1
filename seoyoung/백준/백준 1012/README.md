## 백준 1012 유기농 배추

### 풀이과정

- 처음에는 DFS로 풀었지만 recursion error 나옴
- 백준에서 recursionlimit을 1000으로 처리했는데 최대 50\*50=2500번 recursion 돌 수 있어서 안된듯,,
- DFS -> BFS로 바꿔서 풀어줌

### 코드 구현

사용 언어 : **파이썬**

```python
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
            # 상하좌우 범위를 넘어가거나 배추가 없는 곳이라면(혹은 배추흰지렁이가 이미 살고 있는 곳)
            if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny] == 0:
                continue
            queue.append((nx, ny))
            graph[nx][ny] = 0
    return


for i in range(tc):
    answer = 0
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    # 배추 있는 곳 graph에 표시
    for i in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1

    # 배추밭이면 bfs탐색해서 방문 처리(값을 0으로 만듦) + 배추밭이므로 answer+=1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                answer += 1

    print(answer)

```
