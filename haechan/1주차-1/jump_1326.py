'''백준 1326번 폴짝폴짝

- 최소횟수 + 조건: bfs
- 대강 어떻게 풀어야 한다는 느낌은 왔는데 구현이 안되서 정답 코드 참고했습니다.
- 아직 코드에 대해 100%가 안되네요..
'''
from collections import deque


def get_minCount(n, num_list, a, b):
    dq = deque()
    dq.append(a-1)
    visited = [-1] * n
    visited[a-1] += 1

    while dq:
        node = dq.popleft()
        for i in range(node, n, num_list[node]):
            if visited[i] == -1:
                dq.append(i)
                visited[i] = visited[node] + 1
                print(visited[node], visited[i])
                if i == b-1:
                    return visited[i]
        for n in range(node, -1, -num_list[node]):
            if visited[i] == -1:
                dq.append(i)
                visited[i] = visited[node] + 1
                if i == b-1:
                    return visited[i]
    return -1


n = int(input())
num_list = list(map(int, input().split()))
a, b = map(int, input().split())
print(get_minCount(n, num_list, a, b))