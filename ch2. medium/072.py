from itertools import combinations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

coordinates = [(i, j) for i in range(N) for j in range(N)]


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

answer = 1e9
for combination in combinations(coordinates, 3):
    blossom = set()
    bad = False
    cost = 0
    for (r, c) in combination:
        if (r, c) in blossom:
            bad = True
            break
        blossom.add((r, c))
        cost += A[r][c]
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or N <= nr or nc < 0 or N <= nc:
                bad = True
                break
            if (nr, nc) in blossom:
                bad = True
                break
            blossom.add((nr, nc))
            cost += A[nr][nc]

    if not bad:
        answer = min(answer, cost)

print(answer)