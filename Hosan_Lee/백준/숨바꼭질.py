from collections import deque

From, To = map(int, input().split())
#저는 보통 visited 배열 크기는 { 최대 수 + (전체 수의 범위) /2 }로 설정해놓습니다! 그래야지 에러가 덜 나는 것 같아요.
dq = deque()
visited = [0 for i in range(150000)]
count = 0
answer = -1
dq.append([From, count])
visited[From] = 1
while dq :
    tmp_list = dq.popleft()
    tmp_number = tmp_list[0]
    tmp_count = tmp_list[1]
    if tmp_number == To :
          answer = tmp_count
          break
    else :
        if visited[tmp_number - 1] == 0 and tmp_number - 1 >= 0  :
            dq.append([tmp_number - 1, tmp_count + 1])
            visited[tmp_number-1] = 1
        if visited[tmp_number + 1] == 0 and tmp_number + 1 <= 100000 :
            dq.append([tmp_number + 1, tmp_count + 1])
            visited[tmp_number + 1] = 1
        if tmp_number * 2 <= 100000 :
            if visited[tmp_number * 2] == 0  :
                dq.append([tmp_number * 2, tmp_count + 1])
                visited[tmp_number * 2] = 1
print(answer)