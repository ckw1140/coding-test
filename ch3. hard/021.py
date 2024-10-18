from collections import deque

R, C = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(R)]
adj = {(r, c): [] for r in range(R) for c in range(C)}

dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, -1, 0, 1, -1, 0, 1]

valley = []
for r in range(R):
    for c in range(C):
        min_val = B[r][c]
        who = (-1, -1)
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]

            if nr < 0 or R <= nr or nc < 0 or C <= nc:
                continue

            if min_val > B[nr][nc]:
                min_val = B[nr][nc]
                who = (nr, nc)

        if who != (-1, -1):
            adj[who].append((r, c))
        else:
            valley.append((r, c))


answer = [[0] * C for _ in range(R)]
visit = [[False] * C for _ in range(R)]

for vr, vc in valley:
    queue = deque()
    queue.append((vr, vc))
    visit[vr][vc] = True
    count = 1

    while len(queue) != 0:
        r, c = queue.popleft()

        for (nr, nc) in adj[(r, c)]:
            if not visit[nr][nc]:
                queue.append((nr, nc))
                visit[nr][nc] = True
                count += 1

    answer[vr][vc] = count

for i in range(R):
    print(*answer[i])
    