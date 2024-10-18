from collections import deque

a, k = map(int, input().split())

adj = [[] for _ in range(k + 1)]

for i in range(1, k + 1):
    if i + 1 <= k:
        adj[i].append(i + 1)
    if 2 * i <= k:
        adj[i].append(2 * i)

visit = [False] * (k + 1)
dist = [-1] * (k + 1)
queue = deque()

queue.append(a)
visit[a] = True
dist[a] = 0

while len(queue) != 0:
    u = queue.popleft()

    for v in adj[u]:
        if not visit[v]:
            queue.append(v)
            visit[v] = True
            dist[v] = dist[u] + 1


print(dist[k])