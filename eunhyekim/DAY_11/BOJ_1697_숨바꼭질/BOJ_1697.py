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