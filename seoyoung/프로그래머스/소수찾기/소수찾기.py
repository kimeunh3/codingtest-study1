import itertools


def is_prime_number(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    num_arr = []

    for i in range(1, len(numbers)+1):
        num_arr.append(list(map(''.join, itertools.permutations(numbers, i))))
    num_arr = set(sum(num_arr, []))

    for num in num_arr:
        if is_prime_number(int(num)) and int(num) not in answer:
            answer.append(int(num))

    return len(answer)
