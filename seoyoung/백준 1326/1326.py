# 1326번 폴짝폴짝
from collections import deque

N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
visited = [-1]*(N+1)
flag = False

queue = deque()
queue.append(a)
visited[a] = 0

while queue:
    node = queue.popleft()

    for i in range(1, N+1):
        if (i-node) % bridge[node-1] == 0 and visited[i] == -1:
            queue.append(i)
            visited[i] = visited[node]+1
            if i == b:
                flag = True
                break
    if flag:
        break

print(visited[b])
