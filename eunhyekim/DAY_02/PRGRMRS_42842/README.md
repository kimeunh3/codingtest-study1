## 풀이

우선 brown 수와 yellow 수를 합한 총 격자의 수를 가지는 total을 만들어 주었습니다.  

for loop을 돌려준 height의 범위는 yellow를 적어도 height에 하나는 포함해야하기 때문에 3부터, height는 width보다 길 수 없기 때문에 height와 width의 길이가 같은 경우까지만 돌려주기 위해 total의 제곱근까지입니다.  

그리고 total로 height를 나누었을때 나누어떨어지면서 주어진 brown을 가지는지 확인해주는 check함수에서 true를 받을때 total을 height로 나눈 값인 width와 height를 list에 담아 return해주었습니다.  

check함수는 width, height, brown을 받아 카펫의 테두리 길이에서 두 번 더해진 모서리 부분을 빼주면 brown 수가 나오는데 주어진 brown수와 같은지 확인해주는 함수 입니다.  

## 코드
```python
def check(width, height, brown):
    return brown == 2*width + 2*height - 4

def solution(brown, yellow):
    total = brown + yellow
    for height in range(3, int(total**(1/2))+1):
        if total % height == 0 and check(total//height, height, brown):
            return [total//height, height]
```