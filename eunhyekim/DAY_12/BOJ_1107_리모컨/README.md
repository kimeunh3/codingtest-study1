## 풀이

완전탐색으로 풀어주었습니다.

우선 result를 100에서 N까지의 거리(+던지 -던지 숫자 버튼을 쓰지 않고 채널 변경하는 경우)로 초기화 해주었습니다.
고장난 버튼이 없다면, 숫자 버튼을 눌러서 변경하는 것과 위의 경우 중 최소값을 저장해줍니다.

고장난 버튼이 있을 경우에는 고장난 버튼을 포함하는 모든 채널을 돌아가며,  
그 채널로 바꾸는 데 누르는 버튼의 수(len(str(ch)))와 그 채널과 N까지의 거리(abs(N-ch))를 더한 값을  
현재 result와 비교해 더 작은 값으로 저장해주며 찾았습니다.

## 코드

```python
N = int(input())
M = int(input())

result = abs(100 - N)

if M == 0:
    result = min(result, len(str(N)))
else:
    broken = list(map(int, input().split()))
    # 상한을 500,001으로 두었을때는 아래의 예제를 통과하지 못함
    # 500000
    # 9
    # 0 1 2 3 4 6 7 8 9
    # 예상 출력: 55561 (555,555에서 55,555번 -)
    # 상한 500001의 출력: 444450 (55,555에서 444,445번 +)
    for ch in range(1000000):
        for c in str(ch):
            if int(c) in broken:
                break
        else:
            result = min(result, abs(N-ch)+len(str(ch)))
print(result)
```
