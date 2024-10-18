import heapq

K, N = map(int, input().split())
P = list(map(int, input().split()))

heap = []
for p in P:
    heapq.heappush(heap, p)

v = 0
for _ in range(N):
    v = heapq.heappop(heap)

    for p in P:
        if v * p >= 2 ** 31:
            break
        heapq.heappush(heap, v * p)
        if v % p == 0:
            break

print(v)