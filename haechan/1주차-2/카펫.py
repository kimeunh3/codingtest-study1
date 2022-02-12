''' 프로그래머스 카펫

- 리턴되는 카펫의 가로 x 세로 = brown + yellow라는 점에 착안해서
  brown + yellow의 약수 리스트를 만들고, 조건에 맞는 [가로, 세로]를 반환.
'''

from itertools import combinations

def solution(brown, yellow):
    total = brown + yellow
    num_list = [] # 약수 리스트
    for i in range(1, total): # brown + yellow의 약수를 찾기 위한 반복문
        if total % i == 0:
            num_list.append(i)
        if i * i == total: # 3 * 3과 같은 제곱수 조합을 표현하기 위해 제곱수의 경우 두번 넣음
            num_list.append(i)
            
    combi = list(combinations(num_list, 2)) # 약수의 조합을 만듦
    for nums in combi:
        wid, hei = nums
        if wid * hei == total and (wid-2) * (hei-2) == yellow: # 두가지 조합에 맞는 한 가지 조합을 리턴
            return [max(nums), min(nums)]