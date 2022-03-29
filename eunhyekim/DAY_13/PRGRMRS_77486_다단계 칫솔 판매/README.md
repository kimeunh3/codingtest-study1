## 풀이

우선 `enroll`을 `key`로, `enroll`의 `index`를 `value`로 저장해주는 `idx` 라는 `dictionary`를 만들어주어  
enroll의 이름으로 index를 불러올 수 있게끔 하였습니다.

또한 `answer`는 `enroll`의 길이만큼 0으로 초기화해주었고 `recur` 함수에서 값을 바꿀 수 있도록 `global`로 정의해주었습니다.

`sold`라는 `seller`를 `key`로, 해당 `seller`가 낸 이익인 `amount`에 100을 곱한 `price`를 `list`로 가지는 `defaultdict`을 만들어주었습니다.  
처음에는 `list`가 아닌 `price`값을 누적하여 저장해주었지만,  
누적한 값의 10%가 아닌, 매번 팔았을 때의 값의 10%를 떼어주는 것은 엄연히 다른 값이기 때문에 `list`로 바꿔주었습니다.

해당 사람의 이름을 `key`로, 해당 사람을 소개시켜준 사람을 `value`로 같는 `referred` 라는 `dictionary`도 만들어주었습니다.

더 이상 소개시켜준 사람이 없을 때까지 `recur` 함수를 돌려주어 `answer`에 누적해주었습니다.

또한, `price`가 0일 경우에는 더 이상 떼줄 값이 없기 때문에 바로 멈춰주었습니다.  
이 예외처리가 없을 경우, `recursion`의 `depth`가 한없이 깊어지므로, 꼭 해주어야 했습니다.
마지막에는 민호에게도 떼어주어야 하기 때문에 10%를 제외한 값을 누적해줍니다.

## 코드

```python
from collections import defaultdict

def recur(idx, person, referred, price):
    global answer
    if referred[person] == "-" or price == 0:
        answer[idx[person]] += price-(price//10)
        return
    ref = referred[person]
    percent = price//10
    answer[idx[person]] += price-percent
    recur(idx, ref, referred, percent)

def solution(enroll, referral, seller, amount):
    global answer
    idx = { enroll[i]: i for i in range(len(enroll))}
    referred = {enroll[k]:referral[k] for k in range(len(enroll))}
    answer = [0 for _ in range(len(enroll))]
    sold = defaultdict(list)
    for j in range(len(seller)):
        sold[seller[j]].append(100*amount[j])
    for person, price in sold.items():
        for p in price:
            recur(idx, person, referred, p)

    return answer
```
