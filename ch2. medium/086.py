T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    S = set(A)

    A.sort()
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if 2 * A[j] - A[i] in S:
                count += 1

    print(count)