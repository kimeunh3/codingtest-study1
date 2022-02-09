'''프로그래머스 두개 뽑아서 더하기'''

from itertools import combinations

def solution(numbers):
    combi = list(combinations(numbers, 2))
    
    result_set = set()
    for c in combi:
        if sum(c) not in result_set:
            result_set.add(sum(c))
    
    return sorted(list(result_set))