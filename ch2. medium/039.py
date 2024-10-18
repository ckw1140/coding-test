N = int(input())
A = list(map(int, input().split()))

D = [-1e9] * N
E = [-1e9] * N

D[0] = A[0]
for i in range(1, N):
    D[i] = max(A[i], A[i] + D[i - 1])

E[N - 1] = A[N - 1]
for i in range(N - 2, -1, -1):
    E[i] = max(A[i], A[i] + E[i + 1])

answer = max(D)
for i in range(1, N - 1):
    answer = max(answer, D[i - 1] + E[i + 1])

print(answer)