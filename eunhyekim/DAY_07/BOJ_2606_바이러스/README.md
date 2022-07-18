## 풀이

BFS로 구현했습니다.

인접리스트를 구현해준 뒤, 시작 노드를 queue에 넣고 탐색을 시작합니다. popleft를 해주면서 방문하지 않았다면 해당 노드를 visit에 넣어주고, queue를 해당 노드와 연결된 모든 노드들을 extend로 queue에 추가해주며 돌아주었습니다.

마지막에는 방문해준 노드들의 길이(visit의 길이)를 return 해주었습니다.

visit의 길이는 시작 노드도 포함하기 때문에 1을 빼준 값을 print 해줍니다.

## 코드

```python
from collections import deque
from collections import defaultdict
import sys
input = sys.stdin.readline
def bfs(start):
    visit = []
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            if node in graph:
                queue.extend(graph[node])
    return len(visit)
N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(bfs(1)-1)
```
