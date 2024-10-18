N, m, M, T, R = map(int, input().split())

if m + T > M:
    print(-1)
else:
    timer = 0
    X = m
    while N > 0:
        timer += 1

        if X + T <= M:
            X += T
            N -= 1
        else:
            X -= R
            X = max(X, m)

    print(timer)