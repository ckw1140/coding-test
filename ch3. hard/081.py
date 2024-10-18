T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    adj = [[] for _ in range(N)]
    
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        u, v = u - 1, v - 1

        adj[u].append((v, c, d))

    D = [[1e9] * (M + 1) for _ in range(N)]
    for m in range(M + 1):
        for u in range(N):
            if u == N - 1:
                D[u][m] = 0
                continue
            for v, c, d in adj[u]:
                if c <= m:
                    D[u][m] = min(D[u][m], d + D[v][m - c])

    if D[0][M] == 1e9:
        print("Poor KCM")
    else:
        print(D[0][M])