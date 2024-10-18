from collections import deque


N, M = map(int, input().split())
A = [[0] * M for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))


visit = [[False] * M for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if A[i][j] == 1:
            queue.append((i, j))
            visit[i][j] = True
            dist[i][j] = 0

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

while len(queue) != 0:
    r, c = queue.popleft()

    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or N <= nr or nc < 0 or M <= nc:
            continue
        
        if not visit[nr][nc]:
            queue.append((nr, nc))
            visit[nr][nc] = True
            dist[nr][nc] = dist[r][c] + 1


print(max([max(dist[i]) for i in range(N)]))