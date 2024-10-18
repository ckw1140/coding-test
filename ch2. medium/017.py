N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

D = [[False] * 80002 for _ in range(N)]
zero = 40001
D[0][zero] = True
D[0][zero + A[0]] = True
D[0][zero - A[0]] = True
for i in range(1, N):
    for j in range(0, 80002):
        D[i][j] = D[i - 1][j]

        if j - A[i] >= 0:
            D[i][j] |= D[i - 1][j - A[i]]
        if j + A[i] < 80002:
            D[i][j] |= D[i - 1][j + A[i]]

for i in range(M):
    if D[N - 1][zero + B[i]]:
        print("Y", end=" ")
    else:
        print("N", end=" ")