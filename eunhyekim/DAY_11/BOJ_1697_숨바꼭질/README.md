## 풀이  

BFS로 풀었습니다.  

처음에 visited를 사용하지 않고 풀었을 때는 메모리 초과가 났습니다.  

그래서 visited로 해당 수를 방문해주지 않았을 때만 방문해주었습니다.  

visited에 걸리는 시간을 누적해주었기 때문에 마지막에는 visited\[K\]를 출력해주었습니다.  

## 코드  
```python
from collections import deque

N, K = map(int, input().split())
visited = [0 for _ in range(200001)]
queue = deque([N])
result = 100000

while queue:
    X = queue.popleft()
    if X == K:
        break
    dx = [X + 1, X - 1, X * 2]
    for nx in dx:
        if 0 <= nx < 200001 and not visited[nx]:
            visited[nx] = visited[X] + 1
            queue.append(nx)
        
print(visited[K])
```