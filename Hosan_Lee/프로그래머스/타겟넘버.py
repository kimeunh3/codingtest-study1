def solution(numbers, target):
    global answer
    answer = 0
    DFS_Back(0, 0, [], numbers, target)
    return answer

def DFS_Back(depth, i, count, numbers, target) :
    if depth == len(numbers) :
        if sum(count) == target :
            global answer
            answer += 1
            return
        return
    for j in range(2) :
        if j == 0 :
            count.append(numbers[i])
            DFS_Back(depth+1, i+1, count, numbers, target)
            count.pop()
        if j == 1 :
            count.append(numbers[i] * -1)
            DFS_Back(depth + 1, i + 1, count, numbers, target)
            count.pop()







