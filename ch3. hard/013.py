from queue import PriorityQueue

N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1

    adj[a].append((b, c))
    adj[b].append((a, c))

dist = [[1e9] * N for _ in range(N)]

for s in range(N):
    pq = PriorityQueue()
    pq.put((0, s))
    dist[s][s] = 0

    while pq.qsize() != 0:
        d, u = pq.get()

        for v, w in adj[u]:
            if dist[s][v] > dist[s][u] + w:
                dist[s][v] = dist[s][u] + w
                pq.put((dist[s][v], v))


for i in range(N):
    for j in range(N):
        if i == j:
            print("-", end=" ")
        else:
            for k, w in adj[i]:
                if dist[i][j] == w + dist[k][j]:
                    print(k + 1, end=" ")
                    break
    
    print()