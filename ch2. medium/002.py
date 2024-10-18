N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

D = [[0] * (i + 1) for i in range(N)]
D[0][0] = A[0][0]
for i in range(1, N):
    for j in range(i + 1):
        if j > 0:
            D[i][j] = max(D[i][j], A[i][j] + D[i - 1][j - 1])
        if j < i:
            D[i][j] = max(D[i][j], A[i][j] + D[i - 1][j])

print(max(D[N - 1]))