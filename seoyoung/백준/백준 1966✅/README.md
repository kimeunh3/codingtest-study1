## 백준 1966번 프린터 큐

### 코드 구현

사용 언어 : **파이썬**

```python
from collections import deque

tc = int(input())

for i in range(tc):
    # N = 문서 개수 M=몇번째로 인쇄되었는지가 궁금한 문서의 현재 인덱스
    N, M = map(int, input().split())
    # arr = 현재 큐에 들어와 있는 문서 순서
    arr = list(map(int, input().split()))
    queue = deque()
    # 중요도가 같은 문서들이 있기 때문에 추후에 몇번째로 인쇄되었는지 궁금한 문서의 위치를 명확히 하기 위해
    # queue에 현재 인덱스와 중요도를 함께 넣어줌
    for i in range(N):
        queue.append((i, arr[i]))
    answer = 0
    # 현재 큐에 있는 문서의 최대 중요도
    maxPriority = max(q[1] for q in queue)

    while queue:
        idx,node = queue.popleft()
        # 만약 현재 노드의 중요도 == 최대 중요도
        if node == maxPriority:
            answer += 1
            # 문서를 인쇄하는 시점에서 이 문서가 내가 찾고 있는 문서라면 => while문 빠져나가서 answer 출력하면 됨
            if idx == M:
                break
            # 그렇지 않으면 최대 중요도만 갱신해주고 다시 while문
            maxPriority = max(q[1] for q in queue)
        else:
            # 인쇄할 시점이 아니라면 큐에 다시 넣어줌
            queue.append((idx,node))

    print(answer)


```
