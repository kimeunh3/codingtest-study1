def solution(clothes):
    answer = 1
    clothTypes = {}

    for cloth in clothes:
        if cloth[1] not in clothTypes:
            clothTypes[cloth[1]] = 0
        clothTypes[cloth[1]] += 1

    for t in clothTypes:
        answer *= (clothTypes[t]+1)

    return answer-1
