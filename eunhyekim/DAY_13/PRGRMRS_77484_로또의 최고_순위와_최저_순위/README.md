## 풀이

`Counter` 모듈의 `-`연산을 사용하여 풀어보았습니다.  
우선 `Counter` 모듈을 사용할 시 `+`, `-` 연산에 결과값은 아래와 같습니다.

```python
a, b = Counter("abcc"), Counter("bc")
print(a, b) # Counter({'c': 2, 'a': 1, 'b': 1}) Counter({'b': 1, 'c': 1})
print(a-b) # Counter({'a': 1, 'c': 1})
print(a+b) # Counter({'c': 3, 'b': 2, 'a': 1})
```

`set`으로 `intersection(&)`과 `union(|)`과 비슷해보이지만 `set`에서는 중복된 값을 제외시키기 때문에 이번 문제와는 맞지 않았습니다.

`lottos`와 `win_nums`를 각각 `Counter`모듈을 사용하여 바꿔준 뒤,  
`lottos`의 0의 갯수(`lottos[0]`)를 `zeros`에 저장해줍니다.  
`win_nums`에서 `lottos`를 빼게 되면 `win_nums`에서 `lottos`랑 맞지 않은 값들만 남게 됩니다.  
문제에서 중복되는 숫자는 `lottos`의 0밖에 없다고 했기 때문에 별다른 처리 필요없이 `win_nums`에서 `lottos`를 빼준 `Counter`의 길이는 맞지 않은 숫자들의 개수가 됩니다.  
`matched`에 총 개수인 6에서 맞지 않은 개수(`len(win_nums-lottos)`)를 빼준 값을 저장해줍니다.

최고 순위의 경우는 `zeros`가 모두 맞을 경우, 최저 순위의 경우는 `zeros`가 모두 틀릴 경우입니다.

7에서 맞은 개수를 빼면 해당 등수의 숫자가 나오는 것을 이용하여 `return` 해주었습니다.  
맞은 개수가 1이거나, 아무것도 맞지 않을 경우는 둘 다 6등이므로 예외처리를 해줍니다.

## 코드

```python
from collections import Counter

def solution(lottos, win_nums):
    lottos = Counter(lottos)
    win_nums = Counter(win_nums)
    zeros = lottos[0]
    matched = 6-len(win_nums-lottos)
    return [7-(zeros+matched) if zeros+matched else 6, 7-matched if matched else 6]
```
