# 조합 사용 X

def solution(d, budget):
    d.sort()
    p = [d[0:i+1] for i in range(len(d))]
    answer = list(filter(lambda x: sum(x)<=budget, p))
    return len(answer[-1])
