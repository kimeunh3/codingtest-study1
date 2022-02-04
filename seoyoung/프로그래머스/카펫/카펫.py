def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if yellow % i == 0 and brown == 2*(i+yellow/i)+4:
            answer.append(yellow/i+2)
            answer.append(i+2)
            break

    return answer
