import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
R -= 1
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    adj[u].append(v)
    adj[v].append(u)


visit = [False] * N
D = [0] * N

def dfs(u):
    visit[u] = True

    D[u] = 1
    for v in adj[u]:
        if not visit[v]:
            dfs(v)
            D[u] += D[v]

dfs(R)

for _ in range(Q):
    u = int(input())
    u -= 1

    print(D[u])