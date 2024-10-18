import sys
import heapq

input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

max_pq = [1e9]
min_pq = [1e9]
for i in range(N):
    a = [A[i]]
    a.append(-heapq.heappop(max_pq))
    a.append(heapq.heappop(min_pq))
    a.sort()

    # i + 1 -> (i + 2) // 2 + 1
    pos = 0
    while len(max_pq) < (i + 2) // 2 + 1:
        heapq.heappush(max_pq, -a[pos])
        pos += 1

    while pos < 3:
        heapq.heappush(min_pq, a[pos])
        pos += 1

    print(-max_pq[0])