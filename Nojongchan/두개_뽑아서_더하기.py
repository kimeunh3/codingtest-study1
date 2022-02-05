from itertools import combinations

def solution(numbers):
    arr = list(combinations(numbers, 2))
    answer = list(set([sum(i) for i in arr]))
    answer.sort()
    return answer

    


    


