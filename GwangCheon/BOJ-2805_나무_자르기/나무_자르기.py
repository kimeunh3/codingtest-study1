import sys

N, M = map(int, sys.stdin.readline().split())  # N과 M 값 입력받기

tree_height = list(map(int, sys.stdin.readline().split()))  # 나무들의 높이를 입력

start, end = 1, max(tree_height)

while start <= end:  # 만약 start 보다 end 값이 작아지면 반복 종료
    mid = (start + end) // 2  # 중간 나무 길이
    m = 0
    for tree in tree_height:
        if tree > mid:
            m += (tree - mid)
            
        if m > M:
            break

    if m >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)
