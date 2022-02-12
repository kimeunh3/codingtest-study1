## 백준 2667번 단지번호붙이기

### 알고리즘

- **dfs**

### 풀이 과정

```txt
✅ 집이 있는 곳(graph[x][y]가 1인 곳)이 발견되면 그곳을 기준으로 집이 몇 군데 있는지 찾아내야한다는 점에서 해당 노드를 기준으로 주변 노드를 완벽하게 탐색하는 dfs로 풀어야겠다고 생각함
✅ 집이 있는 곳을 발견하면 전역변수로 선언한 house + 1을 하고 그 주변(노드 기준 상하좌우)을 재귀함수로 탐색함, 탐색 완료 후 true 리턴
✅ 집이 없는 곳이라거나 x,y좌표가 그래프 범위를 넘어가는 경우는 false를 리턴하여 주변을 탐색하지 않고 함수 종료
```

### 코드 구현

사용 언어 : **파이썬**

```python

def dfs(x, y):
    global house

    if x <= -1 or x >= N or y <= -1 or y >= N or graph[x][y] == 0:
        return False

    house += 1
    graph[x][y] = 0
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True

house=0
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
houses = []

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            houses.append(house)
            house = 0

houses.sort()

print(len(houses))
for i in range(len(houses)):
    print(houses[i])

```
