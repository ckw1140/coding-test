N, M = map(int, input().split())

answer = []
name = []
for i in range(N):
    S = input().split()
    name.append(S[-1])
    S = S[:-1]

    max_count = 0
    count = 0
    for i in range(M):
        if S[i] == '.':
            count += 1
        if S[i] == '*':
            count = 0
        
        max_count = max(max_count, count)

    answer.append(max_count)

print(len(set(answer)))
for i in range(N):
    print(answer[i], name[i])