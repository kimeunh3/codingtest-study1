## 단어 정렬 ( 백준 실버 1181번)


### 문제 설명

- 알파벳 소문자로 이루어진 N개의 단어를 입력받는다
- 입력받은 단어들을  길이가 짧은 순으로, 만약 길이가 같다면 사전 순으로 정렬한다.
- 단, 같은 단어가 여러번 입력된 경우에는 한번만 출력된다.


### 자료 구조

- **count_num**
    - 타입 : 정수
    - 저장 데이터 : 입력 받을 문자열의 수를 저장합니다. 

- **save_word**
    - 타입 : 리스트
    - 저장 데이터 : 입력받은 문자열을 저장 합니다.

### 풀이 과정

```txt
1. input을 이용해 count_num에 입력받을 문자열 수를 입력받습니다.

2. 반복문을 통해 count_num 만큼 반복하며 입력받은 문자를 save_word에 저장합니다.

3. save_word 리스트에 중복된 문자열이 있으면 안되므로 set을 통해 중복을 제거해준 후 다시 list로 형변환을 시켜줍니다. 

4. save_word를 Python 내장 메서드인 sort()를 사용하여 사전 순으로 정렬합니다.

5. 사전순으로 정리한 save_word를 sort(key=len) 옵션을 사용해 문자열 길이 순으로 재 정렬 해줍니다.

6. 저장된 리스트를 출력합니다.
```

### 코드 구현
사용 언어 : **파이썬**
```python
# 풀이과정 1
count_num = int(input())
# 풀이과정 2
save_word = []  # 입력 받는 문자를 저장할 리스트

for i in range(count_num):
    save_word.append(input())

"""
중복문자를 제거하기 위해 set 사용 이때, set 을 사용하면 타입이 set 으로 바뀌기 때문에 
list 로 다시 바꿔주기 위해 list 로 형변환 시켜준다.
"""
# 풀이과정 3
save_word = list(set(save_word))
# 풀이과정 4, 5
save_word.sort()  # sort 를 사용해서 사전 순으로 정렬
save_word.sort(key=len)  # sort 에 옵션 key=len 을 추가하여 문자열 길이 순으로 정렬
# 풀이과정 6
for i in save_word:
    print(i)
```
점수 : **100/ 100**
