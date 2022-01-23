import sys
from collections import Counter

n = int(sys.stdin.readline())  # 땅의 개수

for _ in range(n):
    t = list(map(int, sys.stdin.readline().split()))  # 땅의 병사수 및 병사 군대 번호 입력
    land_t = int(t[0]) / 2
    t_list = t[1:]

    max_t = Counter(t_list).most_common(1)

    if max_t[0][1] > land_t:
        print(max_t[0][0])
    else:
        print("SYJKGW")
