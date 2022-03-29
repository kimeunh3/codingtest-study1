'''프로그래머스 - 행렬 테두리 회전하기'''

def rotate_n_get_min(matrix, query):
    x1, y1, x2, y2 = query # 2, 2 / 5, 4
    
    # 윗변부터 시계방향으로
    # 4개의 테두리는 따로 처리, 시계방향으로 왼쪽 위부터 c1, c2, c3, c4
    c1, c2 = matrix[x1][y1-1], matrix[x1-1][y2-2]
    c3, c4 = matrix[x2-2][y2-1], matrix[x2-1][y1]

    numbers_in_query = [c1, c2, c3, c4]
    # 윗변(오른쪽 => 왼쪽 방향)
    for now_y in range(y2-2, y1-1, -1):
        matrix[x1-1][now_y] = matrix[x1-1][now_y-1]
        numbers_in_query.append(matrix[x1-1][now_y])
    # 오른쪽 변(아래 => 위 방향)
    for now_x in range(x2-2, x1-1, -1):
        matrix[now_x][y2-1] = matrix[now_x-1][y2-1]
        numbers_in_query.append(matrix[now_x][y2-1])
    # 아래변(왼쪽 => 오른쪽 방향)
    for now_y in range(y1, y2-1):
        matrix[x2-1][now_y] = matrix[x2-1][now_y+1]
        numbers_in_query.append(matrix[x2-1][now_y])
    # 왼쪽 변(위 => 아래 방향)
    for now_x in range(x1, x2-1):
        matrix[now_x][y1-1] = matrix[now_x+1][y1-1]
        numbers_in_query.append(matrix[now_x][y1-1])
        
    # 테두리 처리
    matrix[x1-1][y1-1], matrix[x1-1][y2-1] = c1, c2
    matrix[x2-1][y2-1], matrix[x2-1][y1-1] = c3, c4
        
    return min(numbers_in_query)


def solution(rows, columns, queries):
    matrix = []
    row = []
    for i in range(1, rows * columns + 1):
        row.append(i)
        if i % columns == 0:
            matrix.append(row)
            row = []
        
    result = []
    for query in queries:
        result.append(rotate_n_get_min(matrix, query))
        
    return result