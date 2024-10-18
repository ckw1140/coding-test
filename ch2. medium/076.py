import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

cache = [[-1] * N for _ in range(N)]
def dp(r, c):
    if cache[r][c] != -1:
        return cache[r][c]

    ret = 1
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or N <= nr or nc < 0 or N <= nc:
            continue
        if F[r][c] < F[nr][nc]:
            ret = max(ret, 1 + dp(nr, nc))

    cache[r][c] = ret
    return ret

print(max([dp(r, c) for r in range(N) for c in range(N)]))