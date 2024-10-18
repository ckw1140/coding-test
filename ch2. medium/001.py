N = int(input())
A = list(map(int, input().split()))

D = [[0] * 1001 for _ in range(N)]

for i in range(1001):
    D[0][i] = 1 if A[0] <= i else 0

for i in range(1, N):
    for j in range(1001):
        D[i][j] = D[i - 1][j]

        if A[i] <= j:
            D[i][j] = max(D[i][j], 1 + D[i - 1][A[i] - 1])

print(D[N - 1][1000])