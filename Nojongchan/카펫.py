a, b = map(int, input().split()) # a = 바깥 사각형  b = 안쪽 사각형

#  바깥사각형 개수 - 4 = 안쪽 사각형 둘레 
#  a - 4 = 안쪽 사각형 둘레 = 2 x (가로+세로)
#  (a - 4) // 2 = 가로 + 세로  ====>  세로 = (a-4) // 2 - 가로

#  width(큰사각형) = 가로 + 2
#  height(큰사각형) = (a-4)//2 - 가로 + 2

# (가로 + 2) * { (a-4)//2 - 가로 + 2 } = b

def solution(brown, yellow):
    for w in range(1, brown):
        h = ((brown - 4) // 2 - w)
        if h * w == yellow:
            return [h+2, w+2]

print(solution(a, b))
    






