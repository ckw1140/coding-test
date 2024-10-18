from collections import deque


M, N = map(int, input().split())
B = [[] for _ in range(N)]

for i in range(N):
    B[i] = list(map(int, input().split()))


visit = [[False] * M for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if B[i][j] == 1:
            queue.append((i, j))
            visit[i][j] = True
            dist[i][j] = 0


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

while len(queue) != 0:
    r, c = queue.popleft()

    for i in range(4):
        if r + dr[i] < 0 or N <= r + dr[i]:
            continue
        if c + dc[i] < 0 or M <= c + dc[i]:
            continue

        if B[r + dr[i]][c + dc[i]] == -1:
            continue

        if not visit[r + dr[i]][c + dc[i]]:
            queue.append((r + dr[i], c + dc[i]))
            visit[r + dr[i]][c + dc[i]] = True
            dist[r + dr[i]][c + dc[i]] = dist[r][c] + 1

max_dist = -1
impossible = False
for i in range(N):
    for j in range(M):
        if B[i][j] == -1:
            continue
        if dist[i][j] == -1:
            impossible = True
            break
        max_dist = max(max_dist, dist[i][j])
    if impossible:
        break

if impossible:
    print(-1)
else:
    print(max_dist)