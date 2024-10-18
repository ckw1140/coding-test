T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    organized = True
    for i in range(N - 1):
        for j in range(M - 1):
            red = A[i][j] + A[i + 1][j + 1]
            blue = A[i + 1][j] + A[i][j + 1]
            if red > blue:
                organized = False
                break

    if organized:
        print("YES")
    else:
        print("NO")