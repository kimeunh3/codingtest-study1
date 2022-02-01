# [문제 풀이] 백준-1326 폴짝폴짝

## 문제 설명
개구리가 일렬로 놓여 있는 징검다리 사이를 폴짝폴짝 뛰어다니고 있다. 
<span style="color:orange;">**징검다리에는 숫자가 각각 쓰여 있는데, 이 개구리는 매우 특이한 개구리여서 어떤 징검다리에서 점프를 할 때는 그 징검다리에 쓰여 있는 수의 배수만큼 떨어져 있는 곳으로만 갈 수 있다.**</span>

이 개구리는 <span style="color:orange;"> **a번째 징검다리에서 b번째 징검다리까지 가려고 한다. 이 개구리가 a번째 징검다리에서 시작하여 <span style= "color:purple">최소 몇 번 점프</span>를 하여 b번째 징검다리까지 갈 수 있는지를 알아보는** </span>프로그램을 작성하시오.

  ---
### 변수 설명
   
   - **N**
    - 타입 : int
    - 저장 데이터 : 징검다리 개수 입력
   
   - **bridge**
    - 타입 : list
    - 저장 데이터 : 각 징검다리마다 갈 수 있는 거리 입력
   
   - **start**
    - 타입 : int
    - 저장 데이터 : 시작지점 입력
   
   - **destination**
    - 타입 : int
    - 저장 데이터 : 도착점
   
   - **dq**
    - 타입 : deque 
    - 저장 데이터 : 징검다리 개수 입력
    
   - **check**
    - 타입 : list
    - 저장 데이터 : 한번 왔던 곳은 체크로 0 데이터 입력 ( 초기 값 : -1 )
  
   - **break_check**
    - 타입 : boolean
    - 저장 데이터 : (초기 값 : false) 이중 for문을 탈출 하기 위한 변수
   
   - **now**
    - 타입 : int
    - 저장 데이터 : 현재 위치한 징검다리
    
 ---
  
   ### 풀이과정
```text
  1. 징검다리 개수 입력받기 (N)
  
  2. 징검다리 마다 갈 수 있는 거리 입력 ( bridge )
  
  3. 출발지, 도착지 입력받기 ( start, destination )
  
  4. deque를 사용하여 큐 생성 ( dq )
  
  5. 시작점을 큐에 넣기 ( dq.append(start - 1) ) \[리스트는 0부터 시작이므로 - 1 ]
  
  6. 한번 방문했던 곳은 check 리스트에 표시하기 (check) \[초기 값을 -1 로하고 들렀던 곳은 업데이트, 시작점은 0으로 업데이트 하고 시작]
  
  7. 큐의 가장 앞에 있는 값을 pop lift 를 통해 받아오기 ( now )
  
  8. 조건문을 통해 이동 가능한 거리 일 경우 위치를 dq에 저장한 후 check 리스트 업데이트
  
  9. 조건문을 통해 현재 위치와 도착점을 비교해서 만약 같다면 중단하고 check 리스트를 통해 걸린 횟수를 출력, 이중 for문을 탈출하기 위해 break_check = True 변환
 
 10. 만약 break_check = True 이면 break
 
 11. 위 7번부터 10번까지 while문을 통해 큐가 빌때 까지 반복
 
 12. 만약 반복문을 모두 돌았는데도 불구하고 check 리스트의 도착점 부분이 -1 로 업데이트가 되어있지 않다면 -1 을 출력 
 ```
  ![](https://images.velog.io/images/soshin_dev/post/5e92c368-4b4b-4a3c-b982-088d75f9e136/KakaoTalk_20220124_145605950.jpg)
  ![](https://images.velog.io/images/soshin_dev/post/81b94b86-fac9-4f83-9b93-909f597692a0/KakaoTalk_20220124_145605950_01.jpg)
  ![](https://images.velog.io/images/soshin_dev/post/b2bf9afe-c8c2-42fd-a863-2162e035bae8/KakaoTalk_20220124_145605950_02.jpg)
  
  ---
### 코드

```python
import sys
from collections import deque

N = int(sys.stdin.readline())  # 징검다리의 개수를 입력
bridge = list(map(int, sys.stdin.readline().split()))  # 징검다리 마다 갈 수 있는 거리 입력
start, destination = map(int, sys.stdin.readline().split())  # 시작점, 도착점 입력

dq = deque()
dq.append(start - 1)  # 시작점을 큐에 넣기
check = [-1] * N  # check 리스트 생성 [ 한번 갔던 곳을 체크하기 위해! ]
check[start - 1] = 0  # 시작점을 check 리스트에 저장

break_check = False  # 이중 for 문을 탈출하기 위한 변수

while dq:  # 큐가 빌 때 까지 반복
    now = dq.popleft()
    for n in range(N):  # 징검 다리 수 만큼 반복 [ 배수만큼 이동 가능하므로 ]
        if (n - now) % bridge[now] == 0 and check[n] == -1:  # 음수로도 이동이 가능하므로 N - now 로 값 지정
            dq.append(n)  # 위치 저장
            check[n] = check[now] + 1  # 체크
            if n == destination - 1:  # 도착점과 현재 위치가 같다면
                print(check[n])
                break_check = True
                break
    if break_check:
        break

if check[destination - 1] == -1:
    print(-1)
```
