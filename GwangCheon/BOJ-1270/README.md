## 문제 설명


현재 여러 지역은 한창 전쟁이 벌어지고 있는 상황인데, 어느 지역은 거의 전쟁이 마무리 단계로 가고 있다.

하지만 당신은 군대를 보낼 때 적군을 혼란시키기 위해서 우리 나라의 군대라는걸 표시하지 않고, <span style="color: orange;">**군대의 번호**</span>로 표시했다.

<span style="color: orange;">**어느 땅에서 한 번호의 군대의 병사가 절반을 초과한다면 그 땅은 그 번호의 군대의 지배하에 놓이게 된다.**</span>

이때, 각 <span style="color: orange;">**땅들을 지배한 군대의 번호를 출력하여라. 만약, 아직 전쟁이 한창중인 땅이라면 “SYJKGW”을 쌍 따옴표 없이 출력한다.**<span>

  ---

### 변수 설명

- **n**
  - 타입 : int - 저장 데이터 : 땅의 개수 입력 후 저장

- **t**
    - 타입 : list
    - 저장 데이터 : 최대 병사 수, 병사들을 한줄에 입력 후 저장
- **land_t**
  - 타입 : int - 저장 데이터 : 땅의 군사 수의 절반을 저장

- **land_dic**
  - 타입 : dictionary - 저장 데이터 : 그 땅의 군대를 키로 받고 그 군대의 병사 수를 value로 저장

 ---

### 풀이과정
```text
1. 땅의 개수 입력 (n)
2. 최대 병사 수, 병사들을 한줄에 입력 (t)
3. land_t 에 땅의 최대 병사의 절반을 저장 이때 정수형이여야 하므로 // 로 나눈다.
4. for문을 통해 len(t)만큼 반복하며 land_dic에 키와 값을 업데이트
5. max_t 에 가장 많은 병사를 가진 key 값을 저장
6. land_t 값 보다 land_dic[max_t] 값이 크면 max_t 값을 출력 작으면 "SYJKGW" 를 출력한다.

**위 과정을 n 만큼 반복**
```
---
   <img src=https://images.velog.io/images/soshin_dev/post/d0e6507c-b6e9-4afa-a863-559208b3f6f6/image.png style="height:700px">
<img src=https://images.velog.io/images/soshin_dev/post/6bc45930-2aa5-4ccc-9fdc-89b20daf592e/image.png style="height:700px">

  
---

### 코드

  ```python
import sys

n = int(sys.stdin.readline())  # 땅의 개수

for _ in range(n):
    t = list(map(int, sys.stdin.readline().split()))  # 땅의 병사수 및 병사 군대 번호 입력
    land_t = t[0] // 2
    land_dic = {}
    for i in range(1, len(t)):
        if t[i] in land_dic:
            land_dic[t[i]] += 1
        else:
            land_dic[t[i]] = 1

    max_t = max(land_dic, key=land_dic.get)

    if land_dic[max_t] > land_t:
        print(max_t)
    else:
        print("SYJKGW")
  ```

  ---
