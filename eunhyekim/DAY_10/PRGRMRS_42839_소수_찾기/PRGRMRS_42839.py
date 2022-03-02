from itertools import permutations

# 소수 판별 함수
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    num_set = []
    for i in range(1, len(numbers)+1):
        # 가능한 조합 모두 찾아주기
        for p in permutations(numbers, i):
            num = int("".join(p))
            # 소수라면 num_set에 넣어주기
            num_set += [ num ] if is_prime(num) else []
    # set으로 중복 제거하기
    num_set = set(num_set)
    return len(num_set)