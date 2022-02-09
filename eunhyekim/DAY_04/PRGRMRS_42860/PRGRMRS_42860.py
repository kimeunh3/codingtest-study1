def solution(name):
    # 가로 움직임
    hori_move = len(name)-1
    # 끝에서부터 A의 개수를 제외
    while name[hori_move] == 'A' and hori_move > 0:
        hori_move -= 1
    # 세로 움직임
    vert_move = 0
    for i, char in enumerate(name):
        vert_move += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 중간에 있는 A 중 마지막 A의 위치
        midA = i + 1
        while  midA < len(name) and name[midA] == 'A':
            midA += 1
        # 아래의 세 가지의 경우를 보고 가장 적은 움직임 고르기
        # 1. hori_move = 돌아가지 않고 앞으로만 간 경우
        # 2. i*2 + (len(name) - midA) = 앞으로 가다가 뒤로 다시 돌아가는 경우
        # 3. (len(name) - midA)*2 + i = 뒤로 먼저 간 뒤 앞으로 다시 돌아오는 경우
        hori_move = min(hori_move, i*2 + (len(name) - midA), (len(name) - midA)*2 + i)
    
    # 가로와 세로 움직임 모두 더한 값을 return
    return hori_move + vert_move