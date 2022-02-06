import sys


def solution(name):
    moves = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    pos = 0

    # 왼쪽으로 쭉 이동 + 오른쪽으로 갔다가 왼쪽으로 이동
    ans1 = sys.maxsize

    for i in range(0, len(moves)):
        pos = 0
        moves1 = moves[:]
        ans_temp = 0
        direction = False
        while True:
            ans_temp += moves1[pos]
            moves1[pos] = 0
            if sum(moves1) == 0:
                break

            if pos == i or pos == i-len(moves):
                direction = True

            # 방향 전환
            if direction:
                pos -= 1
            else:
                pos += 1
            ans_temp += 1
        if ans_temp < ans1:
            ans1 = ans_temp

    # 오른쪽으로 쭉 이동 + 왼쪽으로 갔다가 오른쪽으로 이동
    ans2 = sys.maxsize

    for i in range(len(moves)):
        pos = 0
        moves2 = moves[:]
        ans_temp = 0
        direction = False

        while True:
            ans_temp += moves2[pos]
            moves2[pos] = 0

            if sum(moves2) == 0:
                break

            if pos == i or pos == i-len(moves):
                direction = True

            # 방향 전환
            if direction:
                pos += 1
            else:
                pos -= 1

            ans_temp += 1

        if ans_temp < ans2:
            ans2 = ans_temp

    return min(ans1, ans2)

# def solution(name):
#     answer = 0

#     moves=[min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]

#     pos=0

#     while True:
#         answer+=moves[pos]
#         moves[pos]=0

#         if sum(moves)==0:
#             return answer

#         left=1
#         right=1

#         while moves[pos-left]==0:
#             left+=1

#         while moves[pos+right]==0:
#             right+=1

#         if left<right:
#             answer+=left
#             pos+=-left
#         else:
#             answer+=right
#             pos+=right
