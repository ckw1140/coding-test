from itertools import combinations

N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]
shortcuts = [shortcuts[i] for i in range(N) if shortcuts[i][1] <= D]

min_dist = D
for n in range(N + 1):
    for combination in combinations(shortcuts, n):
        intersect = False
        for i in range(n):
            for j in range(i + 1, n):
                a1, b1, _ = combination[i]
                a2, b2, _ = combination[j]

                if b1 <= a2 or b2 <= a1:
                    continue
                
                intersect = True
                break

        if intersect:
            continue

        dist = D
        for i in range(n):
            a, b, c = combination[i]
            save = b - a - c
            dist -= save

        min_dist = min(min_dist, dist)

print(min_dist)