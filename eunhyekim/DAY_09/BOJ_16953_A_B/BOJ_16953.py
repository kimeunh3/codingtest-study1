import sys

input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1
while A != B:
    if B < A or (B % 10 != 1 and B % 2):
        print(-1)
        break
    B = B // 10 if B % 10 == 1 else B // 2
    cnt += 1
else: print(cnt)