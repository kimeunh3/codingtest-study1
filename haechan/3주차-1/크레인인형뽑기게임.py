'''프로그래머스 크레인 인형 뽑기 게임'''

def solution(board, moves):
    remove_cnt = 0
    stack = [0]
    n = len(board)
    for move in moves:
        x = 0
        move -= 1
        while True:
            before = stack[-1]
            if not board[n-1][move]: # 가장 깊숙한 행에 인형이 없는 경우
                break
            if not board[x][move]: # 첫 행부터 인형 위치 탐색
                x += 1
                continue
            else: # 인형이 있는 행 위치를 찾은 경우
                doll = board[x][move]
                board[x][move] = 0 # 해당 위치의 인형을 빼고
                if doll == before:
                    stack.pop() # 스택에 맨 마지막 인형과 같으면 스택 마지막 삭제
                    remove_cnt += 2
                else:
                    stack.append(doll)
                break
        
    return remove_cnt