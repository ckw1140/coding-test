N, M = map(int, input().split())
B = [input() for _ in range(N)]
K = int(input())

count = {}
for i in range(N):
    zeros = 0
    for j in range(M):
        if B[i][j] == '0':
            zeros += 1

    if zeros % 2 == K % 2 and zeros <= K:
        if B[i] not in count:
            count[B[i]] = 0
        count[B[i]] += 1


max_count = 0
for k, v in count.items():
    max_count = max(max_count, v)

print(max_count)