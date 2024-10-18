from collections import deque

A, B, N, M = map(int, input().split())

adj = [[] for _ in range(100001)]

for i in range(100001):
    if i > 0:
        adj[i].append(i - 1)
    if i < 100000:
        adj[i].append(i + 1)
    if i >= A:
        adj[i].append(i - A)
    if i < 100001 - A:
        adj[i].append(i + A)
    if i >= B:
        adj[i].append(i - B)
    if i < 100001 - B:
        adj[i].append(i + B)
    if i * A < 100001:
        adj[i].append(i * A)
    if i * B < 100001:
        adj[i].append(i * B)

visit = [False] * 100001
dist = [-1] * 100001
queue = deque()

queue.append(N)
visit[N] = True
dist[N] = 0

while len(queue) != 0:
    u = queue.popleft()

    for v in adj[u]:
        if not visit[v]:
            queue.append(v)
            visit[v] = True
            dist[v] = dist[u] + 1

print(dist[M])