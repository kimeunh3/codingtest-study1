## 프로그래머스 카펫

### 코드 구현

사용 언어 : **파이썬**

```python
    answer = []

    # 노란 카펫의 너비와 높이를 찾기 위함
    for i in range(1, yellow + 1):
        # i가 노란 카펫의 너비나 높이가 될 수 있고
        # 그것에 기반한 갈색 카펫의 격자수가 일치한다면 전체 너비와 높이를 answer[]에 넣고 break
        if yellow%i==0 and brown==2*(i+yellow/i)+4:
            answer.append(yellow/i+2)
            answer.append(i+2)
            break

    return answer

```
