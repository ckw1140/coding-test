T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1

        adj[a].append((b, c))
        adj[b].append((a, c))
        
    visit = [False] * N
    D = [0] * N

    def dfs(u):
        visit[u] = True

        is_leaf = True
        for v, w in adj[u]:
            if not visit[v]:
                dfs(v)
                D[u] += min(w, D[v])
                is_leaf = False

        if is_leaf:
            D[u] = 1e9

    dfs(0)
    
    if N == 1:
        print(0)
    else:
        print(D[0])