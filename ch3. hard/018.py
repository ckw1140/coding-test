N, M = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))

D = [[0] * 10001 for _ in range(N)]

for i in range(c[0], 10001):
    D[0][i] = m[0]

for i in range(1, N):
    for j in range(10001):
        D[i][j] = D[i - 1][j]

        if j >= c[i]:
            D[i][j] = max(D[i][j], m[i] + D[i - 1][j - c[i]])

for i in range(10001):
    if D[N - 1][i] >= M:
        print(i)
        break