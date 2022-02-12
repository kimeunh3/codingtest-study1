def solution(n, times):
    answer = 0
    # left: 최소시간, right: 최대 시간
    left = 1; right = min(times)*n
    
    while left <= right:
        # 중앙값: 심사위원에게 주어진 시간
        mid = (left+right)//2
        
        count = 0
        
        for t in times: # t는 각각의 심사관의 심사시간 . .
            count += mid // t   # mid 시간동안 심사관 한명당 처리할수 있는 고객수 .. count에 추가
        
            if count >= n:        
                right = mid-1   
                answer = mid
                break
        
        # mid 시간동안 모든 심사관이 처리할수 있는 숫자보다 고객수가 클 경우
        if count < n:
            left = mid+1

    return answer