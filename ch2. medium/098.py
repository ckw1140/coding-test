from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

def list_to_hash(a):
    hash = 0
    for i in range(len(a)):
        hash += a[i]
        hash *= (len(a) + 1)
    return hash

visit = set()
dist = {}
queue = deque()

queue.append(A)
h_s = list_to_hash(A)
visit.add(h_s)
dist[h_s] = 0

while len(queue) != 0:
    a = queue.popleft()
    h_a = list_to_hash(a)

    for i in range(N - K + 1):
        b = a[:i] + a[i:i + K][::-1] + a[i + K:]
        h_b = list_to_hash(b)
        if h_b not in visit:
            queue.append(b)
            visit.add(h_b)
            dist[h_b] = dist[h_a] + 1

h_t = list_to_hash(list(range(1, N + 1)))
if h_t in dist:
    print(dist[h_t])
else:
    print(-1)