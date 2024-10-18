N, K = map(int, input().split())

A = [0] * N
for i in range(N):
    A[i] = int(input())

dp = [[0] * (K + 1) for _ in range(2)]

for i in range(K + 1):
    if i % A[0] == 0:
        dp[0][i] = 1

for i in range(1, N):
    for j in range(K + 1):
        dp[i & 1][j] = dp[(i - 1) & 1][j]
        if j >= A[i]:
            dp[i & 1][j] += dp[i & 1][j - A[i]]

print(dp[(N - 1) & 1][K])