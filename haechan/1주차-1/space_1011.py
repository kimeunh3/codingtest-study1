'''백준 Fly me to the Alpha Centauri 1011번

- 일반적인 bfs인 줄 알았으나, 범위가 너무 커서 수학적인 규칙이 필요한 문제임을 알았다.(실제로 bfs로 구현하면 메모리 초과 발생)
- x와 y의 거리가 증가함에 따라 count가 일정한 규칙에 따라 증가하는 것을 확인할 수 있다.
- 알았지만 구현이 쉽지 않아서 정답 코드를 참고했습니다. 아직 이해중이네요..
'''

test_case = int(input())
for _ in range(test_case):
    x, y = map(int, input().split())
    dis = y - x
    k = 0
    m = 1
    cnt = 0
    while k < dis:
        k += m
        cnt += 1
        if cnt % 2 == 0:
            m += 1
    print(cnt, end=" ")