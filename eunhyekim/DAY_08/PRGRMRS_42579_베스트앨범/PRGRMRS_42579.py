from operator import itemgetter
from collections import deque

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
        ans.sort(key=itemgetter(1, 0))
        ans = deque(ans)
        album.append(ans.popleft()[0])
        if ans:
            album.append(ans.popleft()[0])
    
    return album