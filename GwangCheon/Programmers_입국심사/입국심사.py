def solution(n, times):
    answer = min(times) * n
    min_time = 1
    max_time = answer
    while min_time < max_time:
        mid = (min_time + max_time) // 2
        temp = 0
        for t in times:
            temp += mid // t
        if temp >= n:
            max_time = mid
            if mid < answer:
                answer = mid
        else:
            min_time = mid + 1
    
    return answer
