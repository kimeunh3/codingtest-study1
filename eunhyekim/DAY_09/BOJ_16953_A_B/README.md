## 풀이  

greedy로 풀었습니다.  

B를 A로 만들어주면서 불가능하면 -1을 return 해주었습니다.  

우선 마지막 숫자가 1일 때는 뒤에 1을 붙여주었을 테니 뒤에 1을 제외해주기 위해 B를 10으로 나눈 값으로 저장해주었습니다.  
그렇지 않을 때는 2로 나눠준 값을 저장해주었고,  
둘 다 해당사항이 없을 때는 A로 만들 수 없으므로 바로 -1을 출력하고 break 해주었습니다.  

while문의 조건을 A와 B가 같지 않은 경우로 해주었기 때문에 break없이 while을 빠져나왔을 때는 A와 B가 같을 경우이므로  
while-else구문으로 cnt를 print해주었습니다.  

## 코드  
```python
import sys

input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1
while A != B:
    if B < A or (B % 10 != 1 and B % 2):
        print(-1)
        break
    B = B // 10 if B % 10 == 1 else B // 2
    cnt += 1
else: print(cnt)
```