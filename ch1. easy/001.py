from itertools import permutations

N, M = list(map(int, input().split()))

for permutations in permutations(range(1, N + 1), M):
    print(*permutations)