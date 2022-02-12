sizes = [[10,7],[12,3],[8,15],[14,7],[5,15]]

for i in range(len(sizes)):
    sizes[i].sort(reverse=True)

a = max(sizes)[0] # 통틀어 가장 긴변 (지갑의 한변의 최솟값)

for i in range(len(sizes)):
    sizes[i].sort()

b= max(sizes)[0] # 짧은 변중에서 그나마 긴변 (지갑의 나머지 한변)

answer = a * b
print(answer)


