def solution(d, budget):
    answer = 0
    total = 0
    d.sort()
    for i in range(len(d)):
        if total + d[i] <= budget:
            total += d[i]
            answer += 1
        else: return answer
    return answer