## 풀이  

아래와 같이 O(N)인 투 포인터 알고리즘으로 시도했지만 런타임 아웃으로 실패했습니다.  
더 빠른 알고리즘이 필요한건가 하고 고민하다 문제 유형이 수학인것을 보고 공식을 찾아야겠다고 생각하게 되었습니다.  
```python
N, L = map(int, input().split())
end = 1
total = 1
sequences = []
for start in range(N//2):
    while total < N and end < N // 2:
        end += 1
        total += end
    if total == N:
        if end-start+1 == L:
            print(" ".join(map(str, range(start, end+1))))
            break
        else:
            if end-start+1 > L:
                sequences.append([end-start+1, (start, end)])
    total -= start
else:
    if len(sequences):
        sequences.sort(key=lambda x: x[0])
        f_start, f_end = sequences[0][1]
        print(" ".join(map(str, range(f_start, f_end+1))))
    else: print(-1)
```
예제들을 보다 보니 패턴을 보였습니다.  
1. 배열의 길이가 홀수일때는 가운데 숫자로 나누어 떨어져야 한다.
2. 배열의 길이가 짝수일때는 가운데 두 숫자의 합으로 나누어 떨어져야한다.

L의 제한은 2부터 100이었으므로 for loop를 주어진 L부터 100까지 돌려주었습니다.  
조건에 맞는 i를 만났을 때, 바로 출력해주고 break를 해주어 더 긴 수열을 찾을 필요가 없게 하였습니다.  

100까지 찾아보아도 찾지 못했을 때는 for-else 구문으로 -1을 출력해주었습니다.  

## 코드  
```python
N, L = map(int, input().split())
for i in range(L, 101):
    if i % 2: # i가 홀수 일때
        if N % i: # 가운데 숫자가 나누어 떨어지지 않을 때
            continue
        start = (N // i)-(i // 2)
        if start < 0: # 시작이 0보다 작을 때
            continue
        print(" ".join(map(str, range(start, start+i))))
        break
    else: # i가 짝수 일때
        if N % (N // i * 2 + 1): # 가운데 두 숫자를 합한 수가 나누어 떨어지지 않을때
            continue
        start = (N // i)-((i // 2) - 1)
        if start < 0: # 시작이 0보다 작을 때
            continue
        print(" ".join(map(str, range(start, start+i))))
        break
else:
    print(-1)
```