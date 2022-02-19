## 풀이  

BFS로 풀어주었습니다.  

방문하는 좌표에 현 좌표값을 누적해 더해주었고 그 결과 해당 좌표에 도달할 수 있는 최소값으로 저장이 됩니다.  

## 코드  
```python
from collections import deque
N, M = map(int, input().split())
graph = [list(map(int,list(input()))) for _ in range(N)]

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

print(graph[N-1][M-1])
```