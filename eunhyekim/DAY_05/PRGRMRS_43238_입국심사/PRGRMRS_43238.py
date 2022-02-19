def solution(n, times):
    answer = 0
    lo, hi = 1, max(times)*n
    while lo <= hi:
        mid = (lo + hi) // 2
        done = 0
        for time in times:
            done += mid // time
            if done >= n:
                break
        if done >= n:
            hi = mid - 1
            answer = mid
        else:
            lo = mid + 1
    return answer