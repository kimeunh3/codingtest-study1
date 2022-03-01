from collections import deque

Num = input().split()
From = int(Num[0])
To = int(Num[1])
result = -1
bfs_stack = deque()
bfs_stack.append([From, 1])
while bfs_stack :
    curr_num, count = bfs_stack.popleft()
    if curr_num == To :
        result = count
        break
    if curr_num * 2 <= To:
        bfs_stack.append([curr_num * 2, count+1])

    if int(str(curr_num) + '1') <= To :
        bfs_stack.append([int(str(curr_num) + '1'), count+1])
print(result)

