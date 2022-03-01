import math


def solution(progresses, speeds):
    duration = []
    answer = []
    for i in range(len(progresses)):
        dur = math.ceil((100-progresses[i])/speeds[i])
        duration.append(dur)

    cnt = 1
    start = duration[0]
    for i in range(1, len(duration)):
        if start >= duration[i]:
            cnt += 1
        else:
            answer.append(cnt)
            start = duration[i]
            cnt = 1
    answer.append(cnt)

    return answer
