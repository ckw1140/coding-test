import sys
from queue import PriorityQueue

input = sys.stdin.readline


N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1

    adj[a].append((b, c))
    adj[b].append((a, c))

S, T = map(int, input().split())
S, T = S - 1, T - 1

dist = [1e9] * N
pq = PriorityQueue()

pq.put((0, S))
dist[S] = 0

while pq.qsize() != 0:
    d, u = pq.get()

    if d != dist[u]:
        continue

    for v, w in adj[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            pq.put((dist[v], v))

print(dist[T])