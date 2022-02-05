import sys


def solution(name):
    moves = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    pos = 0

    # 오른쪽으로 쭉 이동
    ans1 = 0
    moves1 = moves[:]

    while True:
        ans1 += moves1[pos]
        moves1[pos] = 0
        if sum(moves1) == 0:
            break
        pos += 1
        ans1 += 1

    # 왼쪽으로 쭉 이동
    pos = 0
    ans2 = 0
    moves2 = moves[:]

    while True:
        ans2 += moves2[pos]
        moves2[pos] = 0
        if sum(moves2) == 0:
            break
        pos -= 1
        ans2 += 1

    # 오른쪽으로 갔다가 왼쪽으로 이동
    ans3 = sys.maxsize

    for i in range(0, len(moves)):
        pos = 0
        moves3 = moves[:]
        ans_temp = 0
        direction = False
        while True:
            ans_temp += moves3[pos]
            moves3[pos] = 0
            if sum(moves3) == 0:
                break

            if pos == i or pos == i-len(moves):
                direction = True

            # 방향 전환
            if direction:
                pos -= 1
            else:
                pos += 1
            ans_temp += 1
        if ans_temp < ans3:
            ans3 = ans_temp

    # 왼쪽으로 갔다가 오른쪽으로 이동
    ans4 = sys.maxsize

    for i in range(len(moves)-1, -1, -1):
        pos = 0
        moves4 = moves[:]
        ans_temp = 0
        direction = False

        while True:
            ans_temp += moves4[pos]
            moves4[pos] = 0

            if sum(moves4) == 0:
                break

            if pos == i or pos == i-len(moves):
                direction = True

            # 방향 전환
            if direction:
                pos += 1
            else:
                pos -= 1

            ans_temp += 1

        if ans_temp < ans4:
            ans4 = ans_temp

    return min(min(ans1, ans2), min(ans3, ans4))

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
