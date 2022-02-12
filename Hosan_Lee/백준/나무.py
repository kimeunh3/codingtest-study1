import sys

N, M = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(tree)

while start <= end:  # 만약 start 보다 end 값이 작아지면 반복 종료
    mid = (start + end) // 2  # 중간 나무 길이
    m = 0
    for tree in tree:
        if tree > mid:
            m += (tree - mid)

        if m > M:
            break

    if m >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)