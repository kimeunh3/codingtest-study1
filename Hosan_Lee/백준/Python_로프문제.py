import sys

Number_Rope = int(input())

Rope = [int(sys.stdin.readline()) for i in range(Number_Rope)]

Rope.sort()

#삼성 역량테스트 B 이상에서는 sort도 직접 구현하셔야합니다! 이런 경우에는 Merge Sort를 구현하시는게 좋아보여요
#완전탐색

max = 0

for i in range(Number_Rope) :
    tmp = Rope[i] * (Number_Rope-i) # i번째 로프보다 큰 로프의 개수 * i번쨰 로프의 중량
    if max < tmp :
        max = tmp
print(max)





