from queue import PriorityQueue

N, D = map(int, input().split())
adj = [[] for _ in range(D + 1)]

for _ in range(N):
    a, b, c = map(int, input().split())
    if b <= D:
        adj[a].append((b, c))

for i in range(D):
    adj[i].append((i + 1, 1))

dist = [1e9] * (D + 1)
pq = PriorityQueue()
pq.put((0, 0))
dist[0] = 0

while pq.qsize() != 0:
    d, u = pq.get()

    if d != dist[u]:
        continue

    for v, w in adj[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            pq.put((dist[v], v))

print(dist[D])