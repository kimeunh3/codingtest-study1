'''백준 통계학 2108번'''

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n)]

print(round(sum(num_list) / n)) # 산술평균
print(sorted(num_list)[n//2]) # 중앙값

# 최빈값 - dictionary로 정수별  등장횟수 기록
counter_dic = defaultdict(int)
for num in num_list:
    counter_dic[num] += 1

max_value = max(counter_dic.values())
max_numlist = []
for num, cnt in counter_dic.items():
    if max_value == cnt:
        max_numlist.append(num)
if len(max_numlist) != 1:
    print(sorted(max_numlist)[1]) # 최빈값이 여러개인 경우, 두번째로 작은 값
else:
    print(max_numlist[0]) # 최빈값이 하나인 경우

print(max(num_list) - min(num_list)) # 범위