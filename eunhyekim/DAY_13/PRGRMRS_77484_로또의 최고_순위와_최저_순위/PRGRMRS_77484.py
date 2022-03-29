from collections import Counter
def solution(lottos, win_nums):
    lottos = Counter(lottos)
    win_nums = Counter(win_nums)
    zeros = lottos[0]
    matched = 6-len(win_nums-lottos)
    return [7-(zeros+matched) if zeros+matched else 6, 7-matched if matched else 6]