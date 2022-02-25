import operator


def solution(genres, plays):
    answer = []
    totals = {}
    albums = {}

    for i in range(len(genres)):
        if genres[i] not in albums:
            albums[genres[i]] = {}
        albums[genres[i]][i] = plays[i]

    for genre in albums:
        totals[genre] = sum(albums[genre].values())
        albums[genre] = dict(sorted(albums[genre].items(),
                             key=operator.itemgetter(1), reverse=True))
    totals = dict(
        sorted(totals.items(), key=operator.itemgetter(1), reverse=True))

    for genre in totals:
        answer.append(list(albums[genre].keys())[0])
        if len(albums[genre]) > 1:
            answer.append(list(albums[genre].keys())[1])

    return answer
