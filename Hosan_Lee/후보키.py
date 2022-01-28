from itertools import combinations


def solution(relation):
    row, col = len(relation), len(relation[0]) #행과 열 길이
    character = []
    for i in range(1, col + 1):
        character.extend(combinations(range(col), i))

    result = [] #유일성 확인
    for keys in character :
        check = [tuple([S[i] for i in keys]) for S in relation]
        if len(set(check)) == row:
            result.append(keys) #유일한 모든 키들을 result 배열 안에 집어넣는다.

    answer = set(result)  #최소성 확인
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if len(result[i]) == len(set(result[i]).intersection(set(result[j]))): # 조건문,
                answer.discard(result[j])
    return len(answer)