## 풀이

1부터 9까지의 합인 45에서 numbers의 수들을 빼주어 구해주었습니다.   

## 코드
```python
def solution(numbers):
    answer = 45
    for num in numbers: answer -= num
    return answer
```