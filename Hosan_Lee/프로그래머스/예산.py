import math

def solution(d, budget):
    d.sort()
    answer = 0
    hi = len(d)
    lo = 0

    if d[0] > budget :
        return 0
    if sum(d) <= budget :
        return len(d)

    while hi >= lo :

        mid = int((hi + lo) / 2)
        tmp_value = 0

        for i in range(mid) :
            tmp_value += d[i]

        if tmp_value > budget :
            hi = mid - 1
            answer = hi
            tmp = 0
            for i in range(hi) :
                tmp += d[i]
            if tmp == budget :
                return hi
        elif tmp_value <= budget:
            lo = mid + 1
            tmp = 0
            for i in range(lo) :
                tmp += d[i]
            if tmp == budget :
                return lo
            answer = lo - 1

    return answer