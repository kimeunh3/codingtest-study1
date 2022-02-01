'''백준 나무자르기 2805번

- 일반적인 이분탐색 방법으로 탐색 범위를 절반씩 줄여가며 최적의 값을 찾음
'''

import sys

n, m = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))

low = 1
high = max(tree_list)

while low <= high:
    target_len = 0
    mid = (low + high) // 2
    for tree in tree_list:
        if tree > mid:
            target_len += tree - mid
    if target_len < m: # 나무 길이가 목표하는 길이보다 작으면
        high = mid - 1 # 범위를 low ~ mid -1 로 잡아서 자르고자 하는 나무 높이를 낮춘다
    else:
        low = mid + 1

print(high)