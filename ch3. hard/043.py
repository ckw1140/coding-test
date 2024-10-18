T = int(input())
mod = (10 ** 9) + 9

D = [[0] * 1001 for _ in range(1001)]

for i in range(1001):
    D[0][i] = 1
for i in range(1, 1001):
    for j in range(1, 1001):
        D[i][j] = D[i - 1][j - 1]
        if i >= 2:
            D[i][j] += D[i - 2][j - 1]
            D[i][j] %= mod
        if i >= 3:
            D[i][j] += D[i - 3][j - 1]
            D[i][j] %= mod

for _ in range(T):
    N, M = map(int, input().split())
    print(D[N][M])