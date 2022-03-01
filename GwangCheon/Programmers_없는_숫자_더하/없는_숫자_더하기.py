def solution(numbers):
    answer = 0

    for i in range(1, 10):
        if numbers.count(i) <= 0:
            answer += i

    return answer


print(solution([5, 8, 4, 0, 6, 7, 9]))
