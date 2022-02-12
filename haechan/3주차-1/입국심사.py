'''프로그래머스 입국심사'''

def solution(n, times):
    left, right = 1, max(times) * n
    
    while left <= right:
        check_cnt = 0
        mid = (left + right) // 2
        
        for time in times:
            check_cnt += mid // time
        
        if check_cnt < n:
            left = mid + 1
        elif check_cnt >= n: # 최솟값을 찾기 위해 n명을 처리할 수 있는 mid값을 찾았더라도 계속 진행함
            result = mid # 새로운 최솟값이 나올 경우 다시 갱신할 수 있도록
            right = mid - 1
            
    return result