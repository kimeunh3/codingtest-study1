'''프로그래머스 타겟넘버'''

from collections import deque

def solution(numbers, target):
    result = 0
    dq = deque()
    dq.append((numbers[0], 0))
    dq.append((-numbers[0], 0))
    plus_minus = [1, -1]

    while dq:
        num, idx = dq.popleft()
        idx += 1

        if idx < len(numbers): # numbers 리스트 범위 내의 값에 접근
            for i in range(2):
                next_num = numbers[idx] * plus_minus[i]
                dq.append((num+next_num, idx))
        else: # 리스트를 다 순회한 경우
            if num == target:
                result += 1

    return result