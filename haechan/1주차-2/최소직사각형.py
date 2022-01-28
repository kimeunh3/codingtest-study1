''' 프로그래머스 최소 직사각형 

- 지갑의 방향을 돌려서라도 최소 크기의 지갑에 들어가기만 하면 되기 때문에
  [가로, 세로] 리스트에서 큰 값 => list1에, 작은 값 => list2에 넣었습니다.
- 그리고 큰 수들이 모인 list1의 max값 x 작은 수들이 모인 list2의 max값으로 
  모든 명함이 수납되는 가장 작은 지갑의 사이즈를 구했습니다.

'''

def solution(sizes):
    return max([max(size) for size in sizes]) * max([min(size) for size in sizes])