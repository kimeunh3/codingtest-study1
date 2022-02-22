'''프로그래머스 위장'''

from collections import defaultdict

def solution(clothes):
    cnt = 1
    clothes_dic = defaultdict(int)
    for _, cate in clothes:
        clothes_dic[cate] += 1 # 의상의 종류별 개수를 센 딕셔너리 생성
    
    for clothes_num in clothes_dic.values():
        cnt *= clothes_num + 1 # 의상 종류별 경우의 수(의상 1개 입을 경우 + 의상을 하나도 입지 않는 경우)를 곱해 모든 경우의 수를 구한다
    return cnt - 1 # 아무것도 입지 않을 경우를 제외하기 위해 1을 뺀다