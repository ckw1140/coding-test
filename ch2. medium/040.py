N = int(input())
A = list(map(int, input().split()))

D = [-1e9] * N
E = [-1e9] * N

D[0] = A[0]
for i in range(1, N):
    D[i] = max(A[i], A[i] + D[i - 1])
    if i > 1:
        E[i] = max(A[i] + E[i - 1], A[i] + D[i - 2])

print(max(max(D), max(E)))