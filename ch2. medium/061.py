import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    adj = [[] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        adj[y].append(x)

    W = int(input())
    W -= 1

    cache = [-1] * N
    def dp(u):
        if cache[u] != -1:
            return cache[u]

        ret = D[u]
        for v in adj[u]:
            ret = max(ret, dp(v) + D[u])
        cache[u] = ret
        return ret

    print(dp(W))