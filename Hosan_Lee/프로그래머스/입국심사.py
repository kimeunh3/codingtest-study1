def solution(n, times):
    answer = 0
    times.sort()

    hi = times[-1] * n
    lo = 1

    while hi > lo :

        mid = int((hi + lo) / 2) # 총 필요한 시간
        checked = 0
        for i in times :
            checked += mid // i
            if checked >= n :
                break
        if checked < n :
            lo = mid + 1
        if checked >= n :
            hi = mid    #가능한 이유 : mid == 버림, 즉 1씩 계속 낮아진다.
        answer = hi

    return answer