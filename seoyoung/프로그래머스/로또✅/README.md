## 프로그래머스 로또의 최고순위와 최저 순위

### 코드 구현

사용 언어 : **파이썬**

```python
def solution(lottos, win_nums):
    # 안보이는 로또 번호
    unvisible_nums=0
    # 안보이는 로또 번호로 예상할 수 있는 최저 순위가 저장될 grade 변수
    grade=7

    for num in lottos:
        if num==0:
            unvisible_nums+=1
        # num이 win_nums에 포함되어 있으면 등수 -=1
        elif num in win_nums:
            grade-=1

    #최고 순위는 6보다 작을 경우는 최저등수에서 안보이는 로또 번호가 모두 맞았다고 가정해야 하므로 0 개수만큼 빼줌
    # grade-unvisible_nums가 6보다 크면 순위 6이어야 함 <- 7등은 없으므로
    max_grade=grade-unvisible_nums if grade-unvisible_nums<6 else 6
    min_grade=grade if grade<6 else 6

    return [max_grade, min_grade]
```
