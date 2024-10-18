from queue import PriorityQueue

N, K = map(int, input().split())

adj = [[] for _ in range(200001)]

for i in range(200001):
    if i > 0:
        adj[i].append((i - 1, 1))
    if i < 200000:
        adj[i].append((i + 1, 1))
    if 2 * i <= 200000:
        adj[i].append((2 * i, 0))


dist = [1e9] * 200001
pq = PriorityQueue()
pq.put((0, N))
dist[N] = 0

while pq.qsize() != 0:
    d, u = pq.get()

    if d != dist[u]:
        continue

    for v, w in adj[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            pq.put((dist[v], v))

print(dist[K])