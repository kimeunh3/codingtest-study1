# 조합 사용 X
# 오름 차순 정렬하고 원소 개수별로 리스트를 만듬 [x], [x,x], [x,x,x] 

def solution(d, budget):
    d.sort()
    p = [d[0:i+1] for i in range(len(d))]
    answer = list(filter(lambda x: sum(x)<=budget, p))
    return len(answer[-1])
