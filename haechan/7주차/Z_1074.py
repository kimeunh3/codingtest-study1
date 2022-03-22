'''백준 Z 1074번 '''

n, r, c = map(int, input().split())
num = -1 # 순번은 0번부터 시작이므로

def z_recursive(x, y, N):
    global num

    if N == 2: # (r, c)가 있는 사분면에 들어선 경우
        for i in range(x, x + N):
            for j in range(y, y + N):
                num += 1
                if i == r and j == c:
                    print(num)
                    exit(0)
        return

    # 현재 탐색하는 사분면의 범위에 (r, c)좌표가 없으면 
    # 해당 사분면의 칸 개수만큼 순번으로 더한다.
    if not (x <= r < x + N and y <= c < y + N):
        num += N * N
        return

    # 절반씩 탐색범위를 줄여 나가며 (r, c)가 존재하는 사분면을 재귀적으로 탐색
    for i in range(x, x + N, N // 2):
        for j in range(y, y + N, N // 2):
            z_recursive(i, j, N // 2)


z_recursive(0, 0, 2**n)