N = int(input())
A = list(map(int, input().split()))
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    adj[u].append(v)
    adj[v].append(u)

visit = [False] * N
D = [0] * N
E = [0] * N
D_sol = [[] for _ in range(N)]
E_sol = [[] for _ in range(N)]

def dfs(u):
    visit[u] = True

    D[u] = A[u]
    D_sol[u].append(u)
    E[u] = 0
    for v in adj[u]:
        if not visit[v]:
            dfs(v)
            D[u] += E[v]
            D_sol[u].extend(E_sol[v])

            if D[v] < E[v]:
                E[u] += E[v]
                E_sol[u].extend(E_sol[v])
            else:
                E[u] += D[v]
                E_sol[u].extend(D_sol[v])

dfs(0)
if D[0] < E[0]:
    print(E[0])
    E_sol[0].sort()
    print(*list(map(lambda x: x + 1, E_sol[0])))
else:
    print(D[0])
    D_sol[0].sort()
    print(*list(map(lambda x: x + 1, D_sol[0])))