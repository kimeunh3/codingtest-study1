from collections import deque
A, B = map(int, input().split())
answer = -1


def bfs(n):
    global answer
    queue = deque()
    queue.append((n, 1))

    while queue:
        node, cnt = queue.popleft()

        if node == B:
            answer = cnt
            return

        if node*2 <= B:
            queue.append((node*2, cnt+1))
        if node*10+1 <= B:
            queue.append((node*10+1, cnt+1))
    return


bfs(A)
print(answer)
