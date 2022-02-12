import math

def solution(brown, yellow):
    answer = []

    size = brown + yellow

    for i in range(1, math.ceil(size/2)) :
        if size % i != 0 :
            continue
        else :
            height = i
            base = int(size / i)

            if ((height * 2) + (base * 2)) - 4 == brown :
                answer.append(base)
                answer.append(height)
                break

    return answer

brown = int(input())
yellow = int(input())
print(solution(brown, yellow))

#base >= height;