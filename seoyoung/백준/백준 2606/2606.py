from collections import deque

N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]
for i in range(M):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)
answer = 0
visited = []

queue = deque()
queue.append(1)
visited.append(1)

while queue:
    node = queue.popleft()
    for n in graph[node]:
        if n not in visited:
            queue.append(n)
            visited.append(n)
            answer += 1

print(answer)
