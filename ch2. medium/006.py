N = int(input())
par = list(map(int, input().split()))

child = [[] for _ in range(N)]
for i in range(1, N):
    child[par[i]].append(i)


D = [0] * N

def dfs(u):
    times = []
    for v in child[u]:
        dfs(v)
        times.append(D[v])

    times.sort()
    times = times[::-1]

    for i in range(len(times)):
        D[u] = max(D[u], i + 1 + times[i])

dfs(0)
print(D[0])