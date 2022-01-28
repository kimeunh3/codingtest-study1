def solution(brown, yellow):
    for y in range(1, int(yellow ** 0.5) + 1):
        if yellow % y == 0:
            b = yellow // y
            if 2 * y + 2 * b + 4 == brown:
                return [b + 2, y + 2]


print(solution(10, 2))
