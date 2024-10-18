import sys
import heapq

input = sys.stdin.readline


N, Q = map(int, input().split())
A = list(map(int, input().split()))

heap = []
num_zeros = 0
for i in range(N):
    if A[i] == 0:
        num_zeros += 1
    else:
        heapq.heappush(heap, A[i])


for _ in range(Q):
    x, y = map(int, input().split())

    if y == 1:
        continue

    tmp = []
    while len(heap) != 0:
        v = heap[0]
        if v > x:
            break

        heapq.heappop(heap)
        v *= y
        if v == 0:
            num_zeros += 1
        else:
            tmp.append(v)

    for t in tmp:
        heapq.heappush(heap, t)

for i in range(num_zeros):
    print(0, end=" ")

while len(heap) != 0:
    v = heapq.heappop(heap)
    print(v, end=" ")