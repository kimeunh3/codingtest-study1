from collections import Counter

N = int(input())
for _ in range(N):
    troops = list(map(int, input().split()))
    num_troop, troops = troops[0], troops[1:]
    max_troop = Counter(troops).most_common(1)[0]
    result = max_troop[0] if max_troop[1] > num_troop // 2 else "SYJKGW"
    print(result)