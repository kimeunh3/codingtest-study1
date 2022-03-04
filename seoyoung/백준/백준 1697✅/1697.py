from collections import deque
N, K = map(int, input().split())
distance = [0]*100001


def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        node = queue.popleft()

        if node == K:
            print(distance[node])
            break

        for i in (node-1, node+1, node*2):
            if 0 <= i <= 100000 and distance[i] == 0:
                distance[i] = distance[node]+1
                queue.append(i)


bfs(N)
