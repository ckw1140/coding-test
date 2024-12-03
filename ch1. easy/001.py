from itertools import combinations

N, M = map(int, input().split())

for combanation in combinations(range(1, N + 1), M):
    print(*combanation)
