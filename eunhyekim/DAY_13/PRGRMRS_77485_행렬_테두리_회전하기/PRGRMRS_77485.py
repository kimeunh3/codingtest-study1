def rotate(x1, y1, x2, y2):
    global matrix
    x = x1-1
    y = y1-1
    prev = matrix[x][y]
    min_num = prev
    for i in range(y1, y2):
        y = i
        prev, matrix[x][y]  = matrix[x][y], prev
        min_num = min(prev, min_num)
    for j in range(x1, x2):
        x = j
        prev, matrix[x][y]  = matrix[x][y], prev
        min_num = min(prev, min_num)
    for k in range(y2-2, y1-2, -1):
        y = k
        prev, matrix[x][y]  = matrix[x][y], prev
        min_num = min(prev, min_num)
    for l in range(x2-2, x1-2, -1):
        x = l
        prev, matrix[x][y]  = matrix[x][y], prev
        min_num = min(prev, min_num)
    # print(min_num)
    # print(*matrix, sep="\n")
    # print("---------------------")
    return min_num
    
def solution(rows, columns, queries):
    global matrix
    answer = []
    matrix = [[(i-1)*columns+j for j in range(1, columns+1)] for i in range(1, rows+1)]
    for x1, y1, x2, y2 in queries:
        answer.append(rotate(x1, y1, x2, y2))
    return answer