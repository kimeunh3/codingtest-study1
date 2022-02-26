'''백준 차이를 최대로 10819번'''

from itertools import permutations
import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

options = list(permutations(num_list, n)) # 원소 개수만큼 가능한 모든 조합 생성(모든 경우의 수)
max_num = 0
for option in options:
    result_num = 0
    for i in range(len(option)-1):
        result_num += abs(option[i] - option[i+1])
    max_num = max(max_num, result_num) # 주어진 식을 반복하며, 최댓값 갱신
print(max_num)