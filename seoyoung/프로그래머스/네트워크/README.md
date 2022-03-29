## 프로그래머스 네트워크

### 풀이과정

```
- dfs로도 bfs로도 푸는 것이 가능 => bfs로 품
```

### 코드 구현

사용 언어 : **파이썬**

```python
from collections import deque

# 네트워크의 개수를 구하기 위해 컴퓨터들의 연결성 파악해야 함 -> bfs 이용
def bfs(v, visited, computers):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        node = queue.popleft()
        for i in range(len(computers)):
            # computers[i][i]=1인데 사실상 연결된 것이 아니므로 넘어가면 되므로 node!=i 조건 추가해줌
            # node-i가 연결되어 있고 아직 i가 방문처리되지 않았다면
            if node != i and computers[node][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

    return


def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        # i가 아직 방문 전이라면
        if visited[i] == 0:
            # bfs로 i와 연결된 컴퓨터 방문 처리
            bfs(i, visited, computers)
            answer += 1

    return answer
```
