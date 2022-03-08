'''프로그래머스 소수찾기'''

from itertools import permutations

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

def solution(numbers):
    num_list = [num for num in numbers]
    options = [list(permutations(num_list, i)) for i in range(1, len(numbers)+1)] # 전체 조합 리스트 [[('1',), ('7',)], [('1', '7'), ('7', '1')]]
    set_numbers = {int(''.join(num)) for op in options for num in op} # 중복 값 제거한 숫자리스트 {1, 71, 17, 7}
    
    prime_cnt = 0
    for num in set_numbers:
        if num < 2: # 2보다 작은 수는 소수가 아니므로 제외
            continue
        prime_cnt += is_prime(num)
    return prime_cnt