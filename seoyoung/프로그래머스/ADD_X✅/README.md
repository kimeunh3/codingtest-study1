## 프로그래머스 ADD_X

### 코드 구현

사용 언어 : **파이썬**

```python
def solution(numbers):
    answer = 0
    for i in range(1, 10):
        if i not in numbers:
            answer += i
    return answer
```
