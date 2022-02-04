from itertools import combinations


def solution(relation):
    row, col = len(relation), len(relation[0])
    combi = []

    # 속성들의 조합
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))

    result = []
    for c in combi:
        tmp = [tuple([rel[key] for key in c]) for rel in relation]

        # 유일성 확인
        if len(set(tmp)) == row:
            candidate = True

            # 최소성 확인
            for i in result:
                if set(i).issubset(set(c)):
                    candidate = False
                    break

            if candidate:
                result.append(c)

    return len(result)
