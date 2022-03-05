def solution(numbers):
    answer = -1
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in numbers :
        arr[i] = 0
    answer = sum(arr);
    return answer

numbers = [1, 2, 5, 6, 8, 9]
print(solution(numbers));