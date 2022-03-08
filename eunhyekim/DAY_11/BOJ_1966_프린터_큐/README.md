## 풀이  

단순히 구현해주었습니다.  

중요도를 담는 list인 priority와 몇 번째 문서였는지의 정보를 담는 nth_lst를 만들어주었습니다.  

그런 뒤, 지시사항에서 말한대로 가장 앞에 있는 문서의 중요도를 확인하고 나머지 문서들 중 중요도가 더 높은 문서가 있다면 제일 앞에 있던 문서를 제일 뒤로 보냈습니다.  

check_p는 검사해주는 중요도 수치입니다. 9에서부터 줄여가며 체크해주었기 때문에 높은 순서대로 정렬됩니다. check_p가 나머지 문서 중에 없다면 바로 break해주었습니다.  

이미 정렬된 문서는 q_idx를 늘려주어 무시해주었고, 문서 재배치는 slicing으로 해주었습니다.  
priority를 재배치 해줄때 nth_lst도 같이 재배치를 해주어 변경된 순서를 알 수 있게끔 했습니다.  

마지막엔 nth_lst를 돌아주며 M번째 문서를 찾아준 뒤 그 문서의 index에서 1을 더한 값으로 출력해주었습니다.  

## 코드  
```python
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    nth_lst = [i for i in range(N) ]

    for check_p in range(9, -1, -1):
        q_idx = 0
        for _ in range(N):
            if check_p not in priority[q_idx:]:
                break
            if priority[q_idx] < check_p:
                priority = priority[:q_idx] + priority[q_idx+1:] + [priority[q_idx]]
                nth_lst = nth_lst[:q_idx] + nth_lst[q_idx+1:] + [nth_lst[q_idx]]
            else: q_idx += 1
    for idx, val in enumerate(nth_lst):
        if M == val:
            print(idx+1)
            break
```
