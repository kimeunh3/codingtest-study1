## 풀이

가장 앞의 기능이 완료되는 기간을 days에 저장해준 뒤,  
모든 progress들에 days만큼 진행되는 progress를 더해주었습니다.  

앞에서부터 연속되는 배포 가능한 기능(진행상황이 100%이거나 넘는 기능)들의 개수를 세어주었고, answer에 개수를 넣어준 뒤 그 개수만큼 progresses, speeds 둘다 제외시켜주었습니다.   

## 코드
```python
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
```
