### 📔 문제 설명

![](https://images.velog.io/images/soshin_dev/post/7eb38ae4-c8ac-481c-b08b-0c0584bd0163/image.png)
[🧨문제 풀러가기!](https://www.acmicpc.net/problem/1932)

### 🧰 변수 설명

- **N**
    - 타입 : int
    - 저장 데이터 : 삼각형의 크기 입력받아 저장 

- **save**
    - 타입 : list
    - 저장 데이터 : 삼각형 값 입력 받아 저장

- **dp**
    - 타입 : list
    - 저장 데이터 : 더한 값을 저장하는 리스트

### 🖨풀이 과정
1. 삼각형의 크기를 입력 받습니다. \[ N ]

2. 삼각형 내부의 값을 입력 받습니다. \[ save ]
3. 더한 값을 저장하는 DP 리스트를 만듭니다. \[ dp ]
4. 이때 save의 첫 번째 값은 더할 값이 아닌 그대로 값을 넣으므로 save\[0]\[0] 값을 dp\[0]\[0]에 넣습니다.
5. 삼각형 크기 만큼 반복하는 반복문을 생성합니다.
6. 5번에서 만든 반복문의 값을 최대로 가지는 이중 for문을 생성 합니다.
7. 왼쪽 값은 왼쪽끼리 다 더해야 하므로 j == 0 이면 맨 왼쪽을 뜻 하므로 더해줍니다.
8. 오른쪽 값은 오른쪽 끼리 다 더해야 하므로 j == i 이면 맨 오른쪽을 뜻 하므로 더해줍니다.
9. 만약 가운데 값이 존재한다면 왼쪽과 더해준 값과 오른쪽과 더해준 값 중 비교하여 더 큰 값을 dp에 넣습니다.
10. 마지막 최종 값들이 dp의 마지막에 저장되므로 dp\[-1] 값 중 가장 큰 값이 정답이므로 max를 통해 비교해줍니다.

```python
import sys
N = int(sys.stdin.readline())  # 삼각형의 크기 입력
save = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]  # 값 입력

dp = [[0] * i for i in range(1, N + 1)]  # 더한 값을 저장하는 DP 리스트
dp[0][0] = save[0][0]  # 첫 번째 값은 더한 값이 아닌 그대로의 값 이므로 save[0][0] 값을 dp[0][0]에 넣어준다.

for i in range(1, N):  # 삼각형의 크기 만큼 반복
    for j in range(i+1):
        if j == 0:  # 왼쪽 값을 더하기
            dp[i][j] = dp[i-1][j] + save[i][j]
        elif j == i:  # 오른쪽 값을 더하기
            dp[i][j] = dp[i-1][j-1] + save[i][j]
        else:  # 가운데 값을 더할 때, 더 큰값에 더해주기 위해 max 로 비교하기
            dp[i][j] = max(dp[i-1][j-1] + save[i][j], dp[i - 1][j] + save[i][j])

print(max(dp[-1]))
```
메모리 : **38948KB**
시간 : **192ms**
