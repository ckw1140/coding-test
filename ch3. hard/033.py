import sys
import heapq

input = sys.stdin.readline


N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

heap = []
for i in range(1, N - K):
    heapq.heappush(heap, (A[i] - A[i - 1], i - 1))

answer = 1e9
for i in range(0, K + 1):
    # i ~ i + N - K - 1
    M = A[i + N - K - 1] - A[i]
    m, idx = heap[0]

    answer = min(answer, M + m)

    if i != K:
        heapq.heappush(
            heap,
            (A[i + N - K] - A[i + N - K - 1], i + N - K - 1),
        )
        while len(heap) != 0:
            val, idx = heap[0]
            if idx <= i:
                heapq.heappop(heap)
                continue
            break

print(answer)