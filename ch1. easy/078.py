N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    
    adj[u - 1].append((v - 1, w))
    adj[v - 1].append((u - 1, w))


def dfs(u):
    for v, w in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + w
            dfs(v)


for _ in range(M):
    s, t = map(int, input().split())

    dist = [-1] * N
    dist[s - 1] = 0
    dfs(s - 1)

    print(dist[t - 1])