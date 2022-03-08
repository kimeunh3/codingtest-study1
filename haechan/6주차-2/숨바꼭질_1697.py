'''백준 숨바꼭질 1697번'''

from collections import deque

def move_bfs(n, k):
    dq = deque()
    dq.append(n)
    visited = [0] * 100001

    while dq:
        cur = dq.popleft()

        if cur == k:
            return visited[cur]
        
        for _next in [cur+1, cur-1, cur*2]:
            if 0 <= _next < 100001 and not visited[_next]:
                visited[_next] = visited[cur] + 1 # 방문처리 및 count 기록
                dq.append(_next)

n, k = map(int, input().split())
print(move_bfs(n, k))