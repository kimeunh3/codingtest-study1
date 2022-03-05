## 프로그래머스 기능개발

### 코드 구현

사용 언어 : **파이썬**

```python
import math

def solution(progresses, speeds):
    # 작업별 몇 일 후에 배포가 가능한지 저장하는 배열
    duration = []
    answer = []
    # duration 배열 초기화
    for i in range(len(progresses)):
        dur = math.ceil((100-progresses[i])/speeds[i])
        duration.append(dur)
    # 한 번에 배포가 가능한 작업 개수를 저장할 cnt
    cnt = 1
    # start보다 작업 일수가 길다면 => start 배포 시 함께 배포 가능하므로 cnt+=1
    # start보다 작업 일수가 짧은 작업을 만난다면 => 그 작업 전까지 배포 가능하므로 answer에 cnt 넣고, cnt,start 초기화
    start = duration[0]
    for i in range(1, len(duration)):
        if start >= duration[i]:
            cnt += 1
        else:
            answer.append(cnt)
            start = duration[i]
            cnt = 1
    # 마지막 cnt는 answer 배열에 추가하지 못하고 끝나므로 추가
    answer.append(cnt)

    return answer

```
