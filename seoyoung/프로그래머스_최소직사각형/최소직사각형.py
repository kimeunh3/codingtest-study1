def solution(sizes):
    width, height = 0, 0
    for size in sizes:
        w, h = max(size), min(size)
        if width < w:
            width = w
        if height < h:
            height = h

    return width*height
