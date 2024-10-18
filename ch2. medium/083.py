N = int(input())
S = [input() for _ in range(N)]
S = list(set(S))

bad = [False] * len(S)

for i in range(len(S)):
    for j in range(len(S)):
        if i == j:
            continue
        
        if len(S[i]) >= len(S[j]):
            continue

        if S[i] == S[j][:len(S[i])]:
            bad[i] = True

count = 0
for i in range(len(S)):
    if not bad[i]:
        count += 1

print(count)