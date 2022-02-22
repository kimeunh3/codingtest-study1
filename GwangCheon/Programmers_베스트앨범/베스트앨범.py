import operator


def solution(genres, plays):
    answer = []
    list_ge = list(set(genres))  # 장르만 빼오기
    album = {gen: 0 for gen in list_ge}  # 장르: 재생 횟수 의 딕셔너리 생성
    print(album)
    for i in list_ge:  # album 딕셔너리에 장르[Keys]와 재생 횟수[values] 넣기
        for j in range(len(genres)):
            if genres[j] == i:
                album[i] += plays[j]

    album = sorted(album.items(), key=operator.itemgetter(1),
                   reverse=True)  # 딕셔너리를 value 기준으로 정렬하기 itemgetter값이 0 이면 key 기준, 1이면 value 기준!
    best = []

    for i in range(len(genres)):
        best.append({'genres': genres[i], 'plays': plays[i], 'number': i})

    best = sorted(best, key=operator.itemgetter('plays'), reverse=True)  # 많이 재생된 노래 순으로 정렬 [reverse=True로 내림차순 정렬]
    for i in album:  # answer list에 값 넣기 [count를 통해 2개씩 자르기]
        count = 0
        for j in range(len(best)):
            if count == 2:
                count = 0
                break
            if i[0] == best[j]['genres']:
                answer.append(best[j]['number'])
                count += 1

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])