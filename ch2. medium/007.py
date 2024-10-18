N = int(input())
A = list(map(int, input().split()))
K = int(input())

psum = [0] * N
psum[0] = A[0]
for i in range(1, N):
    psum[i] = psum[i - 1] + A[i]

D = [[0] * 4 for _ in range(N)]

for i in range(1, 4):
    D[0][i] = A[0]

for i in range(1, N):
    for j in range(1, 4):
        D[i][j] = D[i - 1][j]
        if i <= K - 1:
            D[i][j] = max(D[i][j], psum[i])
        else:
            sum = psum[i] - psum[i - K]
            D[i][j] = max(D[i][j], sum + D[i - K][j - 1])

print(D[N - 1][3])