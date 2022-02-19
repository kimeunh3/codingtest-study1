from collections import deque
def solution(board, moves):
    answer = 0
    # 뽑은 인형 스택
    stack = []
    for move in moves:
        # board의 move번째 행을 queue로써 가져옵니다.
        # queue의 원소는 인형의 숫자, board에서의 y, x좌표를 가집니다.
        queue = deque([ [board[i][move-1], i, move-1] for i in range(len(board)) if board[i][move-1] ])
        # queue가 비어있지 않다면,
        if len(queue):
            # 가장 위에 있는 인형을 집어줍니다.
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