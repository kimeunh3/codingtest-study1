'''프로그래머스 - 로또의 최고순위와 최저순위'''

def solution(lottos, win_nums):
    result = []
    lotto_rank_dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    matched_cnt = 0
    zero_cnt = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            matched_cnt += 1
        if lotto == 0:
            zero_cnt += 1
    
    result.append(lotto_rank_dic[matched_cnt+zero_cnt])
    result.append(lotto_rank_dic[matched_cnt])
    
    return result
    
    