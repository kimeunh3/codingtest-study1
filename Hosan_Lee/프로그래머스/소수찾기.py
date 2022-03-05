import math
from itertools import permutations

def prime(x) :

    if x == 1 or x == 0:
        return False
    for i in range(2, int(math.sqrt(x)) + 1) :
        if x % i == 0 :
            return False
    return True

def solution(numbers):
    answer = []
    set_answer = set(answer)
    number = []

    for i in range(len(numbers)) :
        number.append((numbers[i]))

    for j in range(1, len(number)+1) :
        for i in permutations(number, j) :

            if prime(int(''.join(i))) == True :
                set_answer.add((int(''.join(i))))
                print(int(''.join(i)))
    return len(set_answer)


print(solution("011"));