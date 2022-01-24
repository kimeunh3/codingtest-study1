# 로프길이를 오름차순으로 정렬
# 로프가 들수있는 무게의 최댓값은 N2

N = int(input())
number_list = [int(input()) for i in range(N)]
number_list.sort()
number_list2 = []

for i in range(N):
    N2 = number_list[i] * (N-i)
    number_list2.append(N2)

print(max(number_list2))