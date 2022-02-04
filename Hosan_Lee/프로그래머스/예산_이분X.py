
def solution(d, budget):
    d.sort()
    count = 0
    answer = 0

    if budget == 0 :
        return 0
    for i in range(len(d)) :
        count += d[i]
        answer += 1
        if count == budget :
            return answer
        elif count > budget :
            return answer - 1

    return answer