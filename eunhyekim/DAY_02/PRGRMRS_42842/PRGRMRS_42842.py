def check(width, height, brown):
    return brown == 2*width + 2*height - 4

def solution(brown, yellow):
    total = brown + yellow
    for height in range(3, int(total**(1/2))+1):
        if total % height == 0 and check(total//height, height, brown):
            return [total//height, height]