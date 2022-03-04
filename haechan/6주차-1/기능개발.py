'''프로그래머스 기능개발'''

from collections import deque

def solution(progresses, speeds):
    done_list = []
    
    # 작업 소요시간 리스트 생성 => [5, 10, 1, 1, 20, 1]
    while len(done_list) != len(progresses):
        for progress, speed in zip(progresses, speeds):
            days = 0
            while progress < 100:
                progress += speed
                days += 1
            done_list.append(days)

    result = []
    while sum(result) != len(progresses):
        now_progress = done_list[0]
        deploy_cnt = 1
        for i in range(1, len(done_list)):
            if now_progress >= done_list[i]:
                deploy_cnt += 1
            else:
                done_list = done_list[i:]
                break
        result.append(deploy_cnt)
        
    return result