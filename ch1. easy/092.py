from itertools import combinations


N, M = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if C[i][j] == 1:
            house.append((i, j))
        if C[i][j] == 2:
            chicken.append((i, j))

min_total = 1e9
for combination in combinations(chicken, M):
    total = 0
    for r1, c1 in house:
        min_dist = 1e9
        for r2, c2 in combination:
            min_dist = min(min_dist, abs(r1 - r2) + abs(c1 - c2))
        total += min_dist
    
    min_total = min(min_total, total)

print(min_total)