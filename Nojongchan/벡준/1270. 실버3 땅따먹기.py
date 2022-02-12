# 절대 이렇게 풀지 마세요.
# 답 확인받는데 5분 걸렸어요.
# 광천님 풀이가 더 아름답습니다.


n = int(input())
ans_list = []


for _ in range(n):
    P = list(map(int, input().split())) # 병사수, 병사 번호
    Q = P[0] // 2         # 과반이 되는 땅 기준
    del P[0]
    
    P.sort()
    count = 1
    for i in range(len(P) - 1):
        if P[i] == P[i+1]:
            count += 1
        if count > Q:
            ans_list.append(P[i])
            break
        if P[i] != P[i+1]:
            count = 1
        if i == len(P) - 2:
            ans_list.append('SYJKGW')
            break

for j in ans_list:
    print(j)

