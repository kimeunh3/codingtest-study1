import sys

n = int(sys.stdin.readline())  # 땅의 개수

for _ in range(n):
    t = list(map(int, sys.stdin.readline().split()))  # 땅의 병사수 및 병사 군대 번호 입력
    land_t = t[0] // 2
    land_dic = {}
    for i in range(1, len(t)):
        if t[i] in land_dic:
            land_dic[t[i]] += 1
        else:
            land_dic[t[i]] = 1

    max_t = max(land_dic, key=land_dic.get)

    if land_dic[max_t] > land_t:
        print(max_t)
    else:
        print("SYJKGW")
