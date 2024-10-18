N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

R = [0] * N
G = [0] * N
B = [0] * N

R[0] = C[0][0]
G[0] = C[0][1]
B[0] = C[0][2]

for i in range(1, N):
    R[i] = C[i][0] + min(G[i - 1], B[i - 1])
    G[i] = C[i][1] + min(R[i - 1], B[i - 1])
    B[i] = C[i][2] + min(R[i - 1], G[i - 1])

print(min(R[N - 1], G[N - 1], B[N - 1]))