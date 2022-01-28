def solution(sizes):
    answer = 0
    width = 0
    height = 0
    
    def change(temp):
        temp[0], temp[1] = temp[1], temp[0]

    for size in sizes:
        if size[0] < size[1]:
            change(size)

        if width < size[0]:
            width = size[0]

        if height < size[1]:
            height = size[1]

    answer = height * width
    return answer


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
