N = int(input())
words = sorted({ input() for _ in range(N) })
cnt = 0
for i in range(len(words)):
    for j in range(i+1, len(words)):
        if words[j][:len(words[i])] == words[i]:
            cnt += 1
            break

print(len(words)-cnt)