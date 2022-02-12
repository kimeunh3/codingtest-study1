# Fly me to the Alpha Centauri

# 최소한의 작동횟수 =
# 중간까지 가속하다가 감속하여 알파센타우리 도착하기 직전 속도는 1이여야 한다!

# 특징: (지구) 1 + 2 + 3 + 4 .... + n + n-1 + n-2  ...... + 1 = n제곱 (도착!)
# 즉 지구와 알파센타우리 거리가 n제곱(각항의 합)일때 2n-1(항의 개수)일 걸린다. 

# 거리가 4일때 : 3일걸림
# 거리가 5일떄 : 4일
# 거리가 6일떄 : 4일
# 거리가 7일떄 : 5일
# 거리가 8일떄 : 5일
# 거리가 9일떄 : 5일걸림 
#
# 즉 2의 제곱이랑 가까울 때는 4일 걸리고 (2를 n이라 보면 2n - 1 + 1)
# 3의 제곱이랑 가까울 떄는 5일 걸리는걸 공유하는걸 알수있다. (2를 n이라 보면 2n + 1)


# 해결책.
# 거리를 구한다
# 거리값을 포함하는 제곱의 범위를 구한다 
# 그 거리값이 어느쪽 제곱에 가까운지 구한다
# 위 식을 참고하여 답을 프린트한다. 



N = int(input())
answer_list = []

for i in range(N):
    a, b = map(int, input().split())
    distance = b-a

    for n in range(66000):
        if n*n < distance <= (n+1)*(n+1):
            if distance <= n*n + n:
                answer_list.append(2*n)
                break
            else: 
                answer_list.append(2*n+1)
                break

for answer in answer_list:
    print(answer)
