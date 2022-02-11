def solution(board, moves):
    doll = []
    answer = 0

    for move in moves:
        for i in range(len(board)): # 몇 번째 칸에 인형이 있는지 모르니 위부터 아래로 순회
            if board[i][move - 1] != 0:
                doll.append(board[i][move - 1])
                board[i][move - 1] = 0

                if len(doll) >= 2: # doll 배열에 2개 이상의 인형이 쌓였다면
                    if doll[-1] == doll[-2]:
                        doll.pop(-1)
                        doll.pop(-1)
                        answer += 2
                break
    return answer