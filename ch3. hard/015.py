from collections import deque

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

low, high = 0, 200
p = -1

while low <= high:
    mid = (low + high) // 2

    found = False
    for min_val in range(200 - mid + 1):
        max_val = min_val + mid

        if A[0][0] < min_val or max_val < A[0][0]:
            continue
        if A[N - 1][N - 1] < min_val or max_val < A[N - 1][N - 1]:
            continue

        visit = [[False] * N for _ in range(N)]
        queue = deque()

        queue.append((0, 0))
        visit[0][0] = True

        while len(queue) != 0:
            r, c = queue.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if nr < 0 or N <= nr or nc < 0 or N <= nc:
                    continue
                if A[nr][nc] < min_val or max_val < A[nr][nc]:
                    continue

                if not visit[nr][nc]:
                    queue.append((nr, nc))
                    visit[nr][nc] = True

        if visit[N - 1][N - 1]:
            found = True
            break

    if found:
        p = mid
        high = mid - 1
    else:
        low = mid + 1

print(p)