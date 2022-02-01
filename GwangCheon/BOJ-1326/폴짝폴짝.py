import sys
from collections import deque

N = int(sys.stdin.readline())  # 징검다리의 개수를 입력
bridge = list(map(int, sys.stdin.readline().split()))  # 징검다리 마다 갈 수 있는 거리 입력
start, destination = map(int, sys.stdin.readline().split())  # 시작점, 도착점 입력

dq = deque()
dq.append(start - 1)  # 시작점을 큐에 넣기
check = [-1] * N  # check 리스트 생성 [ 한번 갔던 곳을 체크하기 위해! ]
check[start - 1] = 0  # 시작점을 check 리스트에 저장

break_check = False  # 이중 for 문을 탈출하기 위한 변수

while dq:  # 큐가 빌 때 까지 반복
    now = dq.popleft()
    for n in range(N):  # 징검 다리 수 만큼 반복 [ 징검다리에서 이동 가능한 거리의 최소 값이 1 이기 때문에  N만큼 반복했을때 도착지에 가능한지 불가능한지 알 수 있다. ]
        if (n - now) % bridge[now] == 0 and check[n] == -1:  # 음수로도 이동이 가능하므로 N - now 로 값 지정
            dq.append(n)  # 위치 저장
            check[n] = check[now] + 1  # 체크
            if n == destination - 1:  # 도착점과 현재 위치가 같다면
                print(check[n])
                break_check = True
                break
    if break_check:
        break

if check[destination - 1] == -1:
    print(-1)
