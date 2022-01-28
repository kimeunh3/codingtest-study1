## 백준 1011번 Fly me to the Alpha Centauri

### 풀이 과정

```txt


```

### 코드 구현

사용 언어 : **파이썬**

```python
    answer = []

    for i in range(1, yellow + 1):
        if yellow%i==0 and brown==2*(i+yellow/i)+4:
            answer.append(yellow/i+2)
            answer.append(i+2)
            break

    return answer

```
