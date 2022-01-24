## 백준 1270번 땅따먹기

### 문제 설명

- 어느 땅에서 한 번호의 군대가 절반을 초과하면 그 번호를 출력
- 그렇지 않다면 “SYJKGW”를 출력

### 자료 구조

- **land_dic** : 딕셔너리({})를 사용해서 시간 복잡도를 단축함

### 풀이 과정

```txt
✅ 리스트 사용 시 시간 초과 발생
✅ for문을 통해 land에 포함된 병사 번호를 land_dic의 키로, 병사의 수를 값으로 하여 land_dic이라는 딕셔너리에 저장하도록 함
✅ 딕셔너리[병사 번호] 값이 과반수를 넘는지 확인하여, 넘는다면 출력하도록 함
✅ break로 for문을 빠져나오는 경우에만 특정 군대의 병사 수가 과반수를 넘어가는 경우이기 때문에 그렇지 않은 경우를 처리하기 위해 flag 변수를 사용함

❗️ Counter 라이브러리를 사용하면 보다 간결하게 풀 수 있음
```

### 코드 구현

사용 언어 : **파이썬**

```python
n = int(input())
for i in range(n):
    land = list(map(int, input().split()))
    # num=병사 수, land=병사 번호 저장된 배열
    num, land = land[0], land[1:]

    # 군대 별 병사 수를 저장하기 위한 딕셔너리
    land_dic = {}
    # break문 빠져나왔는지의 여부를 판단하기 위한 변수
    control = True

    for i in land:
        # land_dic에 군대번호가 키로서 저장되어 있다면
        if i in land_dic:
            # 군대 번호 i 의 병사 수 +1
            land_dic[i] = land_dic[i]+1
            # 군대 번호 i의 병사 수가 과반수를 넘어가면
            if land_dic[i] > num/2:
                print(i)
                control = False
                break
        else:
            land_dic[i] = 1

    # break문으로 빠져나오지 않은 경우 아직 전쟁 중이므로
    if control:
        print("SYJKGW")
```
