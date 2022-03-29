## 프로그래머스 다단계 칫솔 판매

### 코드 구현

사용 언어 : **파이썬**

```python
import math

def solution(enroll, referral, seller, amount):
    #{자식:부모} 형태로 저장되어 있는 parentTree 딕셔너리
    parentTree = dict(zip(enroll, referral))
    # answer에는 {직원 판매 실적 : 0 }으로 초기화
    # 추후 [values,,]로 리스트화시킬 예정
    answer = dict(zip(enroll, [0 for i in range(len(enroll))]))

    for i in range(len(seller)):
        # 이익 earn
        earn=amount[i]*100
        target=seller[i]

        # 이익을 나누어줄 수 있을 때까지 추천인을 타고타고 올라가야 하므로 while문 적용
        while True:
            # 10*0.1은 0이므로 현재 이익이 10보다 작으면 직속 추천인에게 나누어줄 이익 없음
            if earn<10:
                answer[target]+=earn
                break
            # 추천인에게 나누어줄 이익 있는 경우
            else:
                answer[target]+=math.ceil(earn*0.9)
                if parentTree[target]=='-':
                    break
                # earn, target을 추천인 기준으로 다시 설정해주어 while문 돌 수 있게 함
                earn=math.floor(earn*0.1)
                target=parentTree[target]

    return list(answer.values())
```
