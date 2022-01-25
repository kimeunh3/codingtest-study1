import sys
import math

T = int(sys.stdin.readline())  # 테스트 케이스의 개수를 입력

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())  # 현재 위치 x 와 목표 위치 y 입력 [ x는 항상 y보다 작은 값 ]

    d = y - x  # 이동할 거리

    for s in range(1, pow(2, 31)):  # y의 최대 값이 2^31 이므로 2^31 만큼 반복
        if pow(s, 2) > d:  # 만약 현재 속도의 제곱 보다 거리가 크다면
            speed = s - 1  # 그 전 값을 저장
            max_distance = pow(speed, 2)  # 현재 속도의 최대 거리 ( 현재속도의 제곱 )
            count_warp = 2 * speed - 1  # 현 시점 워프 횟수 ( 2 * 현재속도 - 1 )
            distance = d - max_distance  # 남은거리

            count_warp += math.ceil(distance / speed)  # 남은 거리 이동 ( 남은 거리를 최고 속도로 나눈 값을 올림 )
            print(count_warp)
            break

        elif pow(s, 2) % d == 0:  # 현재 속도의 최대 거리가 이동할 거리와 같다면
            print(2 * s - 1)  # 이동할 거리까지 워프한 횟수 출력 ( 2 * 워프 횟수 - 1)
            break
