from itertools import combinations

N, M = map(int, input().split())
A = [[] for _ in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))


max_sum = 0
for combination in combinations(range(M), 3):
    sum = 0
    for i in range(N):
        max_like = 0
        for j in combination:
            max_like = max(max_like, A[i][j])
        sum += max_like

    max_sum = max(max_sum, sum)

print(max_sum)