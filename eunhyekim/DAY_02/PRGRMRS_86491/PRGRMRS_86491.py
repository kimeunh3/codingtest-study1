def solution(sizes):
    width = []
    height = []
    for size in sizes:
        if size[0] < size[1]:
            width.append(size[0])
            height.append(size[1])
        else:
            width.append(size[1])
            height.append(size[0])
    return max(width)*max(height)