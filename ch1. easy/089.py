from collections import deque

N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

visit = [[False] * M for _ in range(N)]
queue = deque()

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

num_pictures = 0
max_count = 0
for i in range(N):
    for j in range(M):
        if B[i][j] == 1 and not visit[i][j]:
            queue.append((i, j))
            visit[i][j] = True
            count = 1
            while len(queue) != 0:
                r, c = queue.popleft()

                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]

                    if nr < 0 or N <= nr or nc < 0 or M <= nc:
                        continue
                    if B[nr][nc] == 1 and not visit[nr][nc]:
                        queue.append((nr, nc))
                        visit[nr][nc] = True
                        count += 1

            max_count = max(max_count, count)
            num_pictures += 1

print(num_pictures)
print(max_count)