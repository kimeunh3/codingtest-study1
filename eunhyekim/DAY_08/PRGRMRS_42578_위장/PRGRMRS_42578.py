from collections import defaultdict

def solution(clothes):
    answer = 1
    kind_dict = defaultdict(int)
    for _, kind in clothes:
        kind_dict[kind] += 1
    keys = list(kind_dict.values())
    for i in range(len(keys)):
        answer *= keys[i]+1

    return answer - 1