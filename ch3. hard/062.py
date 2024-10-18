import sys
from queue import PriorityQueue

input = sys.stdin.readline


N = int(input())
A, B, C = map(int, input().split())
A, B, C = A - 1, B - 1, C - 1
adj = [[] for _ in range(N)]

M = int(input())
for _ in range(M):
    D, E, L = map(int, input().split())
    D, E = D - 1, E - 1

    adj[D].append((E, L))
    adj[E].append((D, L))


dist = [1e9] * N
pq = PriorityQueue()

dist[A], dist[B], dist[C] = 0, 0, 0
pq.put((0, A))
pq.put((0, B))
pq.put((0, C))

while pq.qsize() != 0:
    d, u = pq.get()

    if dist[u] != d:
        continue

    for v, w in adj[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            pq.put((dist[v], v))

max_dist = -1
who = -1
for i in range(N):
    if max_dist < dist[i]:
        max_dist = dist[i]
        who = i

print(who + 1)