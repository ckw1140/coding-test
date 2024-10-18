import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1

    adj[b].append(a)


cache = [-1] * N
def dp(u):
    if cache[u] != -1:
        return cache[u]

    if len(adj[u]) == 0:
        ret = 1
    else:
        ret = max([dp(v) + 1 for v in adj[u]])
    cache[u] = ret
    return ret

for i in range(N):
    print(dp(i), end=" ")