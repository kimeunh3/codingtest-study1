## 풀이

우선, 해당 장르의 곡들을 아래와 같이 **index 0에는 장르의 누적 재생 횟수**를,  
그 다음부터는 **고유번호 i**와 **노래 재생 횟수에 -1을 곱해준 값**을 가지는 tuple을 넣어줍니다.  

매 곡마다 누적 재생 횟수를 갱신하고 tuple을 append해주었습니다.    
```
genre_dict[genre] = [누적 재생 횟수, (고유번호 i, i 노래의 재생 횟수 * -1), ... ]
```
그런 다음에는 dictionary의 value들을 list에 담아 첫 번째 원소인 **누적 재생 횟수가 높은 순**으로 정렬해주었습니다.  

정렬된 list를 돌며, 누적 재생 횟수는 더 이상 필요없으니 list에서 제외 해준 뒤,  
해당 list를 **재생 횟수에따라, 재생 횟수가 같다면 고유 번호에 따라** 정렬해줍니다.  
재생 횟수는 **내림차순**으로, 고유 번호는 **오름차순**으로 정렬해주어야 했기 때문에  
처음에 값을 넣어줄 때 나중에 정렬해주기 편하게 하기 위해 재생 횟수를 **음수**로 바꿔준 뒤, 넣어준 것입니다.  

정렬을 오름차순이 아닌 **내림차순**으로 정렬해주어야 pop을 해준 값이  
장르 내에서 **가장 많이 재생된 노래**이며,  
같은 재생 횟수를 가지는 노래중 **가장 낮은 고유 번호**를 가지게 됩니다.  

고유 번호인 pop해준 값의 **첫번째 원소**를 album list에 넣어준 뒤,  
혹시 해당 장르에 노래가 더 있다면 **한번 더 pop**해주고 고유 번호를 넣어줍니다.  

## 코드
```python
from operator import itemgetter

def solution(genres, plays):
    answer = []
    n = len(plays)
    genre_dict = dict()

    for i, genre in enumerate(genres):
        if genre not in genre_dict:
            genre_dict[genre] = [0]
        genre_dict[genre][0] += plays[i]
        genre_dict[genre].append((i, -1*plays[i]))

    answer = list(genre_dict.values())
    answer.sort(key=itemgetter(0), reverse=True)
    album = []

    for ans in answer:
        ans = ans[1:]
        ans.sort(key=itemgetter(1, 0), reverse=True)
        album.append(ans.pop()[0])
        if ans:
            album.append(ans.pop()[0])
    
    return album
```