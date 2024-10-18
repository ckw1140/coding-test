N = int(input())
A = list(map(int, input().split()))

D = [0] * N
E = [0] * N
F = [0] * N

D[0] = 1
E[0] = 1
F[0] = 1
for i in range(1, N):
    if A[i] == A[i - 1]:
        D[i] = 1
        E[i] = 1 + D[i - 1]
        F[i] = 1 + E[i - 1]
    else:
        D[i] = 1 + D[i - 1]
        E[i] = 1 + E[i - 1]
        F[i] = 1 + F[i - 1]

print(max(max(D), max(E), max(F)))