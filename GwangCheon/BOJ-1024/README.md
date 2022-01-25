## 문제 설명
N과 L이 주어질 때, <span style="color: orange;">**합이 N이면서, 길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램을 작성하시오.**</span>

  ---
### 변수 설명
   
   - **N**
    - 타입 : int
    - 저장 데이터 : 합이 될 수 저장
    
   
   - **L**
    - 타입 : int
    - 저장 데이터 : 최소 길이 값을 저장
    
   
   - **temp**
    - 타입 : str
    - 저장 데이터 : 출력할 문자열을 저장
    
     
   - **x**
    - 타입 : int
    - 저장 데이터 : 계산한 수식을 저장
    
     ---
  
   ### 풀이과정
```text   
1. 합과 최소 길이를 입력 [ N, L ]

2. for문으로 L부터 100까지 반복

3. N-(i*(i+1)) / 2 값을 x에 저장

4. 만약 x가 i로 나누어 떨어지면 x를 i로 나누고 값을 다시 x 에 저장

5. x가 -1 보다 크면 i 만큼 반복하며 j를 더한 값을 문자열로 저장 [ temp ]
```

![](https://images.velog.io/images/soshin_dev/post/541b69c1-32de-43fb-ab44-293ffd1e0fa5/KakaoTalk_20220124_201152509.jpg)
![](https://images.velog.io/images/soshin_dev/post/c41ead3a-8af4-4fd8-adb0-a88ea8eeffff/KakaoTalk_20220124_201152509_01.jpg)

```python
import sys

N, L = map(int, sys.stdin.readline().split())

for i in range(L, 101):  # L은 2보다 크거나 같고, 100보다 작거나 같은 자연수 이기 때문에 100까지만 반복
    x = N - (i * (i + 1) / 2)
    # x = (N - L * ( L + 1) // 2) // L
    temp = ""

    if x % i == 0:
        x = int(x / i)

        if x >= -1:
            for j in range(1, i + 1):
                temp += f"{x + j} "
            print(temp)
            break
else:
    print(-1)
```
