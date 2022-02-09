'''프로그래머스 예산 '''

def solution(d, budget):
    d.sort()
    
    result_set = set()
    for i in range(len(d)+1):
        if sum(d[:i]) <= budget:
            result_set.add(len(d[:i]))
            
    return max(result_set)


def solution(d, budget):
    d.sort()
    result = [len(d[:i]) for i in range(len(d)+1) if sum(d[:i]) <= budget]
            
    return max(result)