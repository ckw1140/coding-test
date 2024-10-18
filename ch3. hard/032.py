import sys

input = sys.stdin.readline


N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]

answer = [['2'] * M for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for r in range(N):
    for c in range(M):
        count = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or N <= nr or nc < 0 or M <= nc:
                continue
            count += 1

        if count % 2 == 1:
            A[r][c] = 'W' if A[r][c] == 'B' else 'B'

for i in range(N):
    for j in range(M):
        if A[i][j] == 'B':
            answer[i][j] = '3'

print(1)
for i in range(N):
    print("".join(answer[i]))