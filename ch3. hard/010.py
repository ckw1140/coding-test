import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, W = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    adj[u].append(v)
    adj[v].append(u)

visit = [False] * N
count = 0

def dfs(u):
    visit[u] = True

    is_leaf = True
    for v in adj[u]:
        if not visit[v]:
            dfs(v)
            is_leaf = False

    if is_leaf:
        global count
        count += 1

dfs(0)

print(W / count)