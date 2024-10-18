from collections import deque

R, C = map(int, input().split())
B = [input() for _ in range(R)]

visit = [[False] * C for _ in range(R)]
queue = deque()

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

final_o = 0
final_v = 0
for i in range(R):
    for j in range(C):
        if B[i][j] != '#' and not visit[i][j]:
            queue.append((i, j))
            visit[i][j] = True
            o_count = 1 if B[i][j] == 'o' else 0
            v_count = 1 if B[i][j] == 'v' else 0

            while len(queue) != 0:
                r, c = queue.popleft()

                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]

                    if nr < 0 or R <= nr or nc < 0 or C <= nc:
                        continue
                    if B[nr][nc] == '#':
                        continue

                    if not visit[nr][nc]:
                        queue.append((nr, nc))
                        visit[nr][nc] = True
                        if B[nr][nc] == 'o':
                            o_count += 1
                        if B[nr][nc] == 'v':
                            v_count += 1

            if o_count > v_count:
                final_o += o_count
            else:
                final_v += v_count

print(final_o, final_v)