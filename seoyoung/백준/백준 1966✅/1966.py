from collections import deque
tc = int(input())

for i in range(tc):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque()
    for i in range(N):
        queue.append((i, arr[i]))
    answer = 0
    maxPriority = max(q[1] for q in queue)

    while queue:
        node = queue.popleft()
        if node[1] == maxPriority:
            answer += 1
            if node[0] == M:
                break
            maxPriority = max(q[1] for q in queue)
        else:
            queue.append(node)

    print(answer)
