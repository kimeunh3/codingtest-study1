'''백준 1270 땅따먹기

- 땅의 개수 n
- i번째 땅의 병사 수, 각 병사의 군대 번호

- 시간초과 문제를 해결하고자 딕셔너리에 저장
'''

n = int(input())
for _ in range(n):
    army_num_lst = list(map(int, input().split()))
    soldier_cnt = army_num_lst.pop(0)
    result_dict = {}

    is_print = False
    for army_num in army_num_lst:
        if army_num not in result_dict.keys():
            result_dict[army_num] = 1
            continue
        result_dict[army_num] += 1
        if result_dict[army_num] > soldier_cnt / 2:
            print(army_num)
            is_print = True
            break
    if not is_print:
        print("SYJKGW")