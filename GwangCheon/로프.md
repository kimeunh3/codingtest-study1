## 문제 설명
N(1 ≤ N ≤ 100,000)개의 로프가 있다. 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.

하지만 여러 개의 로프를 병렬로 연결하면 <span style="color:orange; font-weight:bold">각각의 로프에 걸리는 중량을 나눌 수 있다. k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.</span>

각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 <span style="color:orange; font-weight:bold">물체의 최대 중량을 구해내는 프로그램을 작성하시오. 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.</span>

---
### 변수 설명
   
   - **n**
    - 타입 : 정수
    - 저장 데이터 : 로프의 개수를 저장합니다.
    
   - **rope**
   	- 타입: 리스트
    - 저장 데이터 : 로프가 들수있는 중량을 저장합니다. \[ 다수 입력 ]
    
   - **weight**
   	- 타입: 리스트
    - 저장 데이터 : 반복문을 통해 각 상황마다 들 수 있는 최대무게를 저장 
    
 ---
 ### 풀이과정
 
1. 로프의 개수를 입력 받는다. (n)
2. 각 로프마다 버틸 수 있는 최대 중량을 입력 받는다. (rope)
3. 내림차 순으로 무게를 정렬해준다.
4. n 만큼 반복을 하며 rope\[i] * (i + 1) 의 값을 weight에 저장해준다. (weight)
5. max 메소드를 통해 weight 중 가장 큰 값을 출력한다.
---
<img src=https://images.velog.io/images/soshin_dev/post/84f50cac-b545-4e79-b852-33246b60b3da/image.png style="height:700px">
<img src=https://images.velog.io/images/soshin_dev/post/18bd274f-412a-4cd7-93c0-f873d86e40da/image.png style="height:700px">

---

### 코드
```python
import sys

n = int(input())

rope = [int(sys.stdin.readline()) for i in range(n)]

rope.sort(reverse=True)

weight = [rope[i] * (i + 1) for i in range(n)]
print(max(weight))
```