def crane(board, moves):
    box = []
    doll = 0
    for move in moves:
        for b in range(len(board)):
            # 크레인에 인형이 없는 경우
            if board[b][move - 1] == 0:  # 크레인은 1 ~ 5 까지지만 실제 배열에선 0 ~ 4 이므로 1을 빼준다.
                continue
            # 크레인에 인형이 있을 때
            elif board[b][move - 1] != 0:
                box.append(board[b][move - 1])  # 박스에 값을 넣어준다.
                board[b][move - 1] = 0  # board 에 있는 인형을 빼서 박스에 넣었으므로 0으로 초기화해준다.
                # 바구니 안에 같은 인형이 붙어 있을 경우
                if box[-1:] == box[-2: -1]:
                    doll += 2  # 제거한 인형 수 이므로 2씩 증가
                    box = box[:-2]
                break
    return doll

