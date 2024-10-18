N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

count = [0] * N
for i in range(M):
    for j in range(N):
        if A[j] <= B[i]:
            count[j] += 1
            break

max_vote = 0
who = -1
for i in range(N):
    if max_vote < count[i]:
        max_vote = count[i]
        who = i

print(who + 1)