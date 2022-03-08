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
        # print(priority)
        # print(nth_lst)
    for idx, val in enumerate(nth_lst):
        if M == val:
            print(idx+1)
            break