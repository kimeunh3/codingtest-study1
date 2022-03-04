## 백준 1038번 감소하는 수

### 코드 구현

사용 언어 : **파이썬**

```python
from itertools import combinations

N = int(input())
decreasing = []

# 조합에 쓰일 숫자의 개수 i(1~10)
for i in range(1, 11):
    # 0~9의 숫자에서 i개만큼 숫자를 뽑아서 조합을 만듦
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        # comb를 역순으로 정렬하여 감소하는 수로 만듦
        comb.sort(reverse=True)
        # 배열 형태의 comb를 숫자로 변환하여 decreasing 배열에 삽입
        decreasing.append(int("".join(map(str, comb))))
decreasing.sort()

# 감소수의 총 갯수보다 N이 크면 N번째 감소수가 없다는 이야기이므로 -1출력
if N >= len(decreasing):
    print(-1)
else:
    print(decreasing[N])

```
