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