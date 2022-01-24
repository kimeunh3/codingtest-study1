N, L = map(int, input().split())
for i in range(L, 101):
    if i % 2: # i가 홀수 일때
        if N % i: # 가운데 숫자가 나누어 떨어지지 않을 때
            continue
        start = (N // i)-(i // 2)
        if start < 0: # 시작이 0보다 작을 때
            continue
        print(" ".join(map(str, range(start, start+i))))
        break
    else: # i가 짝수 일때
        if N % (N // i * 2 + 1): # 가운데 두 숫자를 합한 수가 나누어 떨어지지 않을때
            continue
        start = (N // i)-((i // 2) - 1)
        if start < 0: # 시작이 0보다 작을 때
            continue
        print(" ".join(map(str, range(start, start+i))))
        break
else:
    print(-1)