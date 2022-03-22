'''백준 리모컨 1107번

- target_N과 가장 가까운 수 T를 만든다
- (T - target_N)로 차이만큼 버튼을 누른 횟수를 더한다
'''
import sys

target_N = int(sys.stdin.readline())
broken_button_num = int(sys.stdin.readline())
broken_button_list = list(map(int, sys.stdin.readline().split()))

min_count = abs(100 - target_N)

for search_num in range(1000001):
    search_num = str(search_num)
    for i, num in enumerate(search_num):
        if int(num) in broken_button_list:
            break
        elif i == len(search_num) - 1:
            min_count = min(min_count, abs(int(search_num) - target_N) + len(search_num)) # 가장 가까운 숫자 - 타겟 숫자 + 가장 가까운 숫자를 만들기 위해 버튼을 누른 횟수

print(min_count)