T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())

    if M < N:
        M, N = N, M
        x, y = y, x
    
    found = False
    m = y
    for i in range(M):
        if m == x:
            found = True
            print(y + i * N)
            break

        m += N
        if m > M:
            m -= M

    if not found:
        print(-1)