def solution(progresses, speeds):
    answer = []
    time = 0
    cnt = 0

    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                count = 0
            time += 1
    answer.append(cnt)
    return answer