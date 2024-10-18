from collections import deque
from itertools import combinations

N, M = map(int, input().split())
B = [[] for _ in range(N)]

for i in range(N):
    B[i] = list(map(int, input().split()))


cells = [(i, j) for i in range(N) for j in range(M) if B[i][j] == 0]

max_safe = 0
for combination in combinations(cells, 3):
    for row, col in combination:
        B[row][col] = 1

    visit = [[False] * M for _ in range(N)]
    queue = deque()
    for i in range(N):
        for j in range(M):
            if B[i][j] == 2:
                queue.append((i, j))
                visit[i][j] = True

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while len(queue) != 0:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or N <= nr or nc < 0 or M <= nc:
                continue
            if B[nr][nc] == 1:
                continue
            if not visit[nr][nc]:
                queue.append((nr, nc))
                visit[nr][nc] = True

    safe = 0
    for i in range(N):
        for j in range(M):
            if B[i][j] == 0 and not visit[i][j]:
                safe += 1

    max_safe = max(max_safe, safe)

    for row, col in combination:
        B[row][col] = 0

print(max_safe)