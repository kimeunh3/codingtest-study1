## 풀이

board의 move번째 행을 queue로써 가져옵니다.  
queue의 원소는 인형의 숫자, board에서의 y, x좌표를 가집니다.  
```python
board = [[0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]
move = 3
# queue[n] = [board[y][move-1], y, move-1] 
queue = [[1, 1, 2],
        [5, 2, 2],
        [4, 3, 2],
        [1, 4, 2]]
```
queue가 비어있지 않다면, 가장 위에 있는 인형을 집어준 뒤, 집어준 인형의 좌표를 0으로 설정해줍니다.  
stack의 마지막 인형과 같은지 확인해주고 같다면 인형은 터트려져 사라집니다.  
그렇지 않을 경우에는 인형을 stack에 추가해줍니다.  

인형이 터트려져 사라질 때 answer에 2씩 더해주며 사라진 인형의 개수를 update해줍니다.  

모든 move가 끝난 뒤 answer를 return해줍니다.  

## 코드
```python
from collections import deque
def solution(board, moves):
    answer = 0
    # 뽑은 인형 스택
    stack = []
    for move in moves:.
        queue = deque([ [board[i][move-1], i, move-1] for i in range(len(board)) if board[i][move-1] ])
        if len(queue):
            picked, y, x= queue.popleft()
            # 인형은 stack으로 옮겨질테니 인형의 좌표를 0으로 설정합니다.
            board[y][x] = 0
            # stack의 마지막으로 추가된 인형이 집어준 인형과 같다면
            # 인형은 터트려져 사라집니다.
            # 그렇지 않을 경우에는 인형을 stack에 추가해줍니다.
            if len(stack) > 0 and stack[-1] == picked:
                stack.pop()
                answer += 2
            else:
                stack.append(picked)
    return answer
```
