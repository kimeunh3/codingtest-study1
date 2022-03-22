# 3:13PM 시작
# 4:13PM 현 솔루션대로는 불가능 하다고 판단 힌트보고 완전탐색으로 전환
# 4:52PM 성공

# 같은 자리수에서만 비교 가능한 솔루션 아래와 같은 반례는 통과하지 못함
# 99999
# 2
# 8 9
# 예상 출력: 7 (100000에서 한번 -)
# N = input()
# M = int(input())

# result = abs(100 - int("".join(N)))

# if M == 0:
#     result = min(result, len(N))
# else:
#     broken = list(input().split())
#     not_broken = [ number for number in "0123456789" if number not in broken]
#     cnt = 0
#     found = False
#     channel = "0"
#     larger = False
#     if not_broken:
#         for i, num in enumerate(N):
#             if num in broken or found:
#                 if not found:
#                     not_broken.sort(key=lambda x:abs(int(num)-int(x)))
#                     if int(num)-int(not_broken[0]) > 0:
#                         larger = True
#                     channel += not_broken[0]
#                     found = True
#                 else:
#                     if larger:
#                         not_broken.sort(reverse=True)
#                     else:
#                         not_broken.sort()
#                     channel += not_broken[0]
#             else:
#                 channel += num
#             cnt += 1
#     cnt += abs(int("".join(N))-int(channel))
#     result = min(result, cnt)

# print(result)

N = int(input())
M = int(input())

result = abs(100 - N)

if M == 0:
    result = min(result, len(str(N)))
else:
    broken = list(map(int, input().split()))
    # 상한을 500,001으로 두었을때는 아래의 예제를 통과하지 못함
    # 500000
    # 9
    # 0 1 2 3 4 6 7 8 9
    # 예상 출력: 55561 (555,555에서 55,555번 -)
    # 상한 500001의 출력: 444450 (55,555에서 444,445번 +)
    for ch in range(1000000):
        for c in str(ch):
            if int(c) in broken:
                break
        else:
            result = min(result, abs(N-ch)+len(str(ch)))
print(result)
