def solution(sizes):
    answer = 0
    length = len(sizes)
    base = []
    height = []
    for i in range(length) :
       if sizes[i][0] > sizes[i][1] : #큰 애들은 base에, 작은 애들은 height에 저장
           base.append(sizes[i][0])
           height.append(sizes[i][1])
       else :
           base.append(sizes[i][1])
           height.append(sizes[i][0]) #저장 완료

    answer = max(base) * max(height)
    return answer



