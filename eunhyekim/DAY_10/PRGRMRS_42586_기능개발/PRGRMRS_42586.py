def solution(progresses, speeds):
    answer = []
    cnt = 0
    while progresses:
        # 가장 앞의 기능이 완료되는 기간
        days = (100 - progresses[0]) // speeds[0]
        if (100 - progresses[0]) % speeds[0]:
            days += 1
        # days만큼 진행되는 progress 업데이트
        for i in range(len(speeds)):
            progresses[i] += speeds[i]*days
        # 앞에서부터 연속되는 배포 가능한 기능들 세어주기
        for j in range(len(speeds)):
            if progresses[j] < 100:
                break
            cnt += 1
        answer.append(cnt)
        # 배포한 기능들 제외해주기
        progresses = progresses[cnt:]
        speeds = speeds[cnt:]
        cnt = 0
    return answer