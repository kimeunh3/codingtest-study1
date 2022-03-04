## 풀이

완전탐색으로 permutation을 이용해 모든 가능한 수를 찾아주었습니다.  

소수를 판별하는 함수를 따로 만들어주었고, 함수 내에서 제곱근만큼만 돌려주어 효율을 높였습니다.  

소수라면 num_set에 넣어주고 마지막에는 중복제거를 위해 set으로 바꿔준 뒤 길이를 return 해주었습니다.  

## 코드
```python
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
```