from collections import deque

N = int(input())
steps = list(map(int, input().split()))
src, dest = map(int, input().split())
visited = [0 for _ in range(N)]
queue = deque([[src, 0, visited]])
dist = N+1

while queue:
    step, jumps, visited = queue.popleft()
    visited[step-1] = 1
    if steps[step-1] == 1:
       dist = min(jumps+1, dist)
    if step != dest and jumps < dist:
        for i in range(step, N+1, steps[step-1]):
            if not visited[i-1]:
                queue.append((i, jumps+1, visited))
        for j in range(step, 0, -steps[step-1]):
            if not visited[j-1]:
                queue.append((j, jumps+1, visited))
    else:
        dist = min(jumps, dist)
     
if dist == N+1: print(-1)
else: print(dist)