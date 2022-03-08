'''백준 프린터 큐 1966번'''

from collections import deque

result = []
test_case = int(input())
for i in range(test_case):
    n, m = map(int, (input().split()))
    importance_list = list(map(int, (input().split())))

    if n == 1: # 문서가 1개인 경우, 첫번째로 인쇄된다.
        result.append(1)
        continue
    
    # 문서 중요도와 꺼내야 되는 문서를 표시한 queue 생성
    # deque([(1, False), (2, False), (3, True), (4, False)])
    dq = deque()
    for idx, imp in enumerate(importance_list):
        if idx == m:
            dq.append((imp, True))
            continue
        dq.append((imp, False))
    print(dq)

    doc_cnt = 0
    while dq:
        cur_imp, bool = dq.popleft()

        # queue에서 꺼낸 값이 마지막 큐인 경우 --> 해당 문서가 꺼내야 하는 문서
        # 이 예외처리를 안해줘 아래에서 valueError 발생...
        if len(dq) == 0: 
            doc_cnt += 1
            break

        # 꺼낸 문서의 중요도보다 높은 중요도를 가진 문서가 있는 경우, 순서를 맨 뒤로 이동한다.
        if cur_imp < max(dq)[0]:
            dq.append((cur_imp, bool))
            continue
        
        doc_cnt += 1 # 인쇄한 문서 수 누적
        if bool: # 찾고자 하는 값인 경우
            break
    result.append(doc_cnt)

for i in result:
    print(i)