N = int(input())
M = int(input())

D = [[0] * (M + 1) for _ in range(N)]

for i in range(1, M + 1):
    D[0][i] = 1
for i in range(1, N):
    for j in range(M + 1):
        D[i][j] = 0

        for k in range(1, j + 1):
            D[i][j] += D[i - 1][j - k]

print(D[N - 1][M])