# 6:40 PM 시작
# 7:20 PM 제출했지만 시간초과
# 8:00 PM 풀이 찾아서 제출

N, r, c = map(int, input().split())

cnt = 0
def divide(n, y, x):
    global cnt
    if y == r and x == c:
        print(cnt)
        exit(0)
    if n == 1:
        cnt += 1
    else:
        if y+n > r and x+n > c:
            n //= 2
            divide(n, y, x)
            divide(n, y, x+n)
            divide(n, y+n, x)
            divide(n, y+n, x+n)
        else:
            cnt += n*n # 사각형의 크기만큼 늘려주기

divide(2**N, 0, 0)

