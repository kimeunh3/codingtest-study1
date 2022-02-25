## 백준 1141 접두사

### 코드 구현

사용 언어 : **파이썬**

```python
N = int(input())
arr = []
for i in range(N):
    arr.append(input())

# 문자열 정렬을 해서 인접한 문자열이 접두어-단어 관계가 되는지 확인함
arr.sort()
# 전체 배열이 어떤 한 단어가 다른 단어의 접두어가 되는 관계더라도 answer은 1이상이므로 포함시켜주고 시작
answer = 1

for i in range(len(arr)-1):
    # 앞의 단어가 뒤의 단어의 접두사가 아니면 answer+=1
    if arr[i+1].startswith(arr[i]) == False:
        answer += 1

print(answer)
```
