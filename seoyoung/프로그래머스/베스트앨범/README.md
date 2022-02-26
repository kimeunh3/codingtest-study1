## 프로그래머스 베스트앨범

### 코드 구현

사용 언어 : **파이썬**

```python
import operator

def solution(genres, plays):
    answer = []
    # genre별 총 재생 횟수를 저장한 딕셔너리
    totals={}
    # genre별 {고유번호: 재생횟수...}가 저장된 딕셔너리
    albums={}

    # albums={classic:{0:500,2:150,,}} 이런 형태로 저장하는 코드
    for i in range(len(genres)):
        if genres[i] not in albums:
            albums[genres[i]]={}
        albums[genres[i]][i]=plays[i]

    # totals={classic:1450,,} 형태로 저장한 이후 재생 순 장르 정렬
    # albums 장르별 재생 순 노래 정렬
    for genre in albums:
        totals[genre]=sum(albums[genre].values())
        albums[genre]=dict(sorted(albums[genre].items(), key=operator.itemgetter(1),reverse=True))
    totals=dict(sorted(totals.items(), key=operator.itemgetter(1),reverse=True))

    # 재생순으로 정렬된 장르 기준으로 2곡씩(1곡만 있으면 한 곡만) answer에 고유 번호 삽입
    for genre in totals:
        answer.append(list(albums[genre].keys())[0])
        if len(albums[genre])>1:
            answer.append(list(albums[genre].keys())[1])

    return answer
```
