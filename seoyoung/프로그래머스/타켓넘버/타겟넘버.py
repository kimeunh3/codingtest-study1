answer = 0


def dfs(depth, number, numbers, target):
    global answer
    if depth == len(numbers):
        if number == target:
            answer += 1
        return

    dfs(depth+1, number+numbers[depth], numbers, target)
    dfs(depth+1, number-numbers[depth], numbers, target)


def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer
