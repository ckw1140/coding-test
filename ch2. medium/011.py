import sys
sys.setrecursionlimit(10**9)

N = int(input())
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1

    adj[u].append((v, w))
    adj[v].append((u, w))


visit = [False] * N
dist = [0] * N

def dfs(u):
    visit[u] = True
    for v, w in adj[u]:
        if not visit[v]:
            dist[v] = dist[u] + w
            dfs(v)

dfs(0)

max_dist = 0
who = 0
for i in range(N):
    if dist[i] > max_dist:
        max_dist = dist[i]
        who = i

visit = [False] * N
dist = [0] * N
dfs(who)

max_dist = 0
for i in range(N):
    if dist[i] > max_dist:
        max_dist = dist[i]

print(max_dist)