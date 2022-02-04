Num_length = int(input())
Array = list(map(int, input().split()))
a, b, c, d = list(map(int, input().split()))
Min = 1000000001
Max = -1000000001
result = Array[0]

def min_max_DFS(Plus, Minus, Mul, Div, depth) :
    global result
    if Plus == Minus == Mul == Div == 0 :
        global Min
        global Max
        if Min > result :
            Min = result
        if Max < result :
            Max = result
        return

    if Plus > 0:
            tmp = result
            result = result + Array[depth]
            min_max_DFS(Plus - 1, Minus, Mul, Div, depth + 1)
            result = tmp
    if Minus > 0:
            tmp = result
            result = result - Array[depth]
            min_max_DFS(Plus, Minus - 1, Mul, Div, depth + 1)
            result = tmp
    if Mul > 0 :
            tmp = result
            result = result * Array[depth]
            min_max_DFS(Plus, Minus, Mul - 1, Div, depth + 1)
            result = tmp
    if Div > 0 :
            tmp = result
            result = int(result / Array[depth])
            min_max_DFS(Plus, Minus, Mul, Div - 1, depth + 1)
            result = tmp

min_max_DFS(a, b, c, d, 1)
print(Max)
print(Min)


