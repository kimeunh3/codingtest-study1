## 풀이

`rotate`이라는 함수를 따로 만들어주었습니다.

`rotate`은 주어진 전역변수 `matrix`를 주어진 범위 내의 테두리에 위치한 수만 한 칸씩 돌려 값을 저장해줍니다.  
또한 돌려지는 값들 중 가장 작은 수인 `min_num`을 찾아 `return` 해줍니다.

해당 `query` 마다 `rotate`함수를 호출해 `return` 받은 값을 `answer`에 `append` 해준 뒤 `return` 해줍니다.

## 코드

```python
def rotate(x1, y1, x2, y2):
    global matrix
    x = x1-1
    y = y1-1
    prev = matrix[x][y]
    min_num = prev
    # 오른쪽
    for i in range(y1, y2):
        y = i
        prev, matrix[x][y]  = matrix[x][y], prev
        min_num = min(prev, min_num)
    # 아래쪽
    for j in range(x1, x2):
        x = j
        prev, matrix[x][y]  = matrix[x][y], prev
        min_num = min(prev, min_num)
    # 왼쪽
    for k in range(y2-2, y1-2, -1):
        y = k
        prev, matrix[x][y]  = matrix[x][y], prev
        min_num = min(prev, min_num)
    # 위쪽
    for l in range(x2-2, x1-2, -1):
        x = l
        prev, matrix[x][y]  = matrix[x][y], prev
        min_num = min(prev, min_num)
    # print(min_num)
    # print(*matrix, sep="\n")
    # print("---------------------")
    return min_num

def solution(rows, columns, queries):
    global matrix
    answer = []
    matrix = [[(i-1)*columns+j for j in range(1, columns+1)] for i in range(1, rows+1)]
    for x1, y1, x2, y2 in queries:
        answer.append(rotate(x1, y1, x2, y2))
    return answer
```
