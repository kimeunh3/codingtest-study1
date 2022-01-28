''' 프로그래머스 후보키'''

from itertools import combinations

def solution(relation):
    # 유일성 조건: 모든 row 중에서 각 컬럼 당 중복되는 값이 하나도 없는 유일한 값
    # 최소성 조건: 꼭 필요한 조건들로만 구성된 값들
    
    row_num = len(relation)
    col_num = len(relation[0]) # 컬럼 개수

    # 가능한 column 조합 생성
    col = list(range(col_num))
    combi = []
    for i in range(1, col_num+1):
        combi.extend(combinations(col,i)) # 1부터 한개씩 늘려가며 컬럼개수만큼의 조합을 만든다.
    
    # 유일성
    unique_list = []
    for keys in combi:
        data_set = set()
        for row in relation:
            set_str = '' # 2개 이상의 조건인 경우, 문자열로 붙여서 유일성을 판별하기 위함
            for key in keys:
                set_str += row[key]
            data_set.add(set_str)
        if len(data_set) == row_num: # 유일한 데이터의 수가 행의 개수와 같으면 유일성 조건 통과
            unique_list.append(keys)
    
    # 최소성
    final = set(unique_list)
    for i, uni in enumerate(unique_list):
        for uni_next in unique_list[i+1:]:
            if len(set(uni) & (set(uni_next))) == len(uni): # 집합 1 이 집합 2에 완전히 속한다면 집합 2를 제거하는 방식으로 하나씩 제거
                final.discard(uni_next)
    return len(final) # 남은 후보키 조합의 길이가 곧 최대 개수