'''백준 2217번 로프

- 무게를 역순으로 정렬
- (순차적으로 순회하면서 다음으로 큰 무게를 버틸 수 있는 로프 x 사용한 로프 수)를 통해 사용한 로프 수에 따른 최대 중량을 구하고 리스트에 저장
- 가장 큰 무게 리턴
'''

n = int(input())
lope_lst = sorted([int(input()) for _ in range(n)], reverse=True)

max_weight_lst = []
for i in range(n):
    max_weight = lope_lst[i] * (i + 1)
    max_weight_lst.append(max_weight)
print(max(max_weight_lst))