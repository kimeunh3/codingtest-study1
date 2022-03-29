from collections import deque


def bfs(v, visited, computers):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        node = queue.popleft()
        for i in range(len(computers)):
            if node != i and computers[node][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

    return


def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i] == 0:
            bfs(i, visited, computers)
            answer += 1

    return answer
