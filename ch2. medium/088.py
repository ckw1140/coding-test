from collections import deque

N, M = map(int, input().split())
B = [list(map(int, input())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

answer = 0
for i in range(N):
    for j in range(M):
        while True:
            visit = [[False] * M for _ in range(N)]
            queue = deque()

            queue.append((i, j))
            visit[i][j] = True
            ground = False

            while len(queue) != 0:
                r, c = queue.popleft()

                if r == 0 or r == N - 1 or c == 0 or c == M - 1:
                    ground = True
                    break

                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]

                    if nr < 0 or N <= nr or nc < 0 or M <= nc:
                        continue
                    if B[i][j] < B[nr][nc]:
                        continue

                    if not visit[nr][nc]:
                        queue.append((nr, nc))
                        visit[nr][nc] = True

            if ground:
                break
            else:
                B[i][j] += 1
                answer += 1

print(answer)