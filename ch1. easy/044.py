import heapq

N = int(input())
heap = []

for i in range(N):
    a = list(map(int, input().split()))

    for j in a:
        if len(heap) < N:
            heapq.heappush(heap, j)
        else:
            if heap[0] < j:
                heapq.heappop(heap)
                heapq.heappush(heap, j)

print(heap[0])