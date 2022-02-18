## 백준 2178번

### 알고리즘

- **bfs**

### 코드 구현

사용 언어 : **파이썬**

```python
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
            # x,y좌표 기준 상하좌우 좌표
            nx = x+dx[i]
            ny = y+dy[i]
            # (nx,ny)가 그래프를 벗어나지 않고, graph[nx][ny]==1이라면(=이동할 수 있는 칸인데다가, 아직 방문하지도 않았음)
            if nx >= 0 and nx < N and ny >= 0 and ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y]+1


bfs(0, 0)
print(graph[N-1][M-1])
```
