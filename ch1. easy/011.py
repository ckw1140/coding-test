from itertools import combinations

N, S = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for n in range(1, N + 1):
    for combination in combinations(A, n):
        if sum(combination) == S:
            count += 1

print(count)