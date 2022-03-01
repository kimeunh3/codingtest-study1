## 풀이  

BFS로 풀었습니다.  

M*N의 크기를 가지는 2차원 배열 graph를 만들어 준 뒤, 배추가 있는 좌표에 1을 넣어주었습니다.

만들어진 graph를 가지고 1이 있는 좌표를 찾아주어 queue에 넣고 BFS를 시작합니다.  
상하좌우를 다 비교해준 뒤 배추가 있는 좌표를 발견하면 queue에 넣어주고 graph에서 1이었던 것을 0으로 바꿔주어 중복된 좌표를 다시 돌지 않게끔 했습니다. 넣어줄 때 0으로 바꿔주지 않으면 다른 좌표에서 다시 같은 곳을 돌게 되기 때문입니다.

다 돌면 한 블럭을 찾았으니 1을 return 해주었고, 블럭을 찾아낼때마다 return 한 1을 누적하여 출력해주었습니다. 

## 코드  
```python
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
```
