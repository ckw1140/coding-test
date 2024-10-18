T =int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    D = [0] * N
    D[0] = A[0]
    for i in range(1, N):
        D[i] = max(A[i], A[i] + D[i - 1])

    print(max(D))