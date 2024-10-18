N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

D = [[0] * M for _ in range(N)]

answer = 0
for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if B[i][j] != 0:
            continue

        if i == N - 1 or j == M - 1:
            D[i][j] = 1
            answer = max(answer, D[i][j])
            continue

        if D[i + 1][j] == D[i][j + 1]:
            if B[i + D[i + 1][j]][j + D[i + 1][j]] == 0:
                D[i][j] = D[i + 1][j] + 1
            else:
                D[i][j] = D[i + 1][j]
        else:
            D[i][j] = min(D[i + 1][j] + 1, D[i][j + 1] + 1)

        answer = max(answer, D[i][j])

print(answer)