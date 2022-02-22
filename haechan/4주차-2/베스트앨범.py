'''프로그래머스 베스트앨범'''

from collections import defaultdict

def solution(genres, plays):
    playlist_dict = defaultdict(list) # 장르별 재생횟수 리스트
    plays_sum_dict = defaultdict(int) # 재생횟수가 많은 순 장르 정렬
    
    # 각 딕셔너리 생성
    for i in range(len(genres)):
        plays_sum_dict[genres[i]] += plays[i]
        playlist_dict[genres[i]].append((plays[i], i))
    
    # 장르별 재생횟수 리스트 정렬 => {'classic': [(800, 3), (500, 0), (150, 2)], 'pop': [(2500, 4), (600, 1)]}
    for count_list in playlist_dict.values():
        count_list.sort(key=lambda x: (-x[0], x[1])) # 재생횟수: 클수록 앞에, 인덱스: 작을수록 앞에
        
    # 누적 재생횟수가 많은 순으로 장르 정렬한 리스트 생성 => [('pop', 3100), ('classic', 1450)]
    genre_list = [(key, val) for key, val in plays_sum_dict.items()]
    genre_list.sort(key=lambda x: (-x[1]))

    # 누적 재생횟수가 많은 장르부터 최대 2곡의 인덱스 값을 result 리스트에 이어 붙인다
    result = []
    for genre, _ in genre_list:
        result.extend([i[1] for i in playlist_dict[genre][:2]])
            
    return result