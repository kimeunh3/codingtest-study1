def solution(numbers, target):
    answer = 0  # 최종 타겟 넘버 가능 수를 저장할 변수
    result = [0]  # 계산 결과를 담을 리스트
    for num in numbers:  # 값을 하나씩 비교하기 위해 for 문 사용
        temp = []  # 임시 저장 리스트 변수
        for r in result:  # 각 값 마다 더하고 빼고를 반복하기위해 반복
            temp.append(r + num)
            temp.append(r - num)
        result = temp
        
    for r in result:  # 순회하며 타켓 값과 같은 값이 있을 경우 카운트 증가
        if r == target:
            answer += 1
    return answer


