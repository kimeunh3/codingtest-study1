from itertools import permutations
import math


def decimal(n):
    for i in range(2, int(math.sqrt(n)) + 1):  # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True


def permutations_num(num):
    per_num = []
    for i in range(1, int(num) + 1):
        per_num += set((permutations(num, i)))
    return per_num


def solution(numbers):
    answer = 0
    per_num = set(permutations_num(numbers))
    per_num = set(map(int, map("".join, per_num)))

    for s in per_num:
        if s == 0 or s == 1:
            continue
        if decimal(s):
            answer += 1

    return answer

