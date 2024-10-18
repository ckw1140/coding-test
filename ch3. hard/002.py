import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    adj[a].append(b)
    adj[b].append(a)

visit = [False] * N
sizes = [0] * N

def dfs(u):
    visit[u] = True
    sizes[u] = 1

    for v in adj[u]:
        if not visit[v]:
            dfs(v)
            sizes[u] += sizes[v]

dfs(0)

answer = 0
for i in range(1, N):
    answer += sizes[i] * (sizes[i] - 1) // 2
    answer += sizes[i] * (N - sizes[i])

print(answer)