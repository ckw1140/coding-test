from queue import PriorityQueue

N, M = map(int, input().split())
A = list(map(int, input().split()))

pq = PriorityQueue()
for x in A:
    pq.put(x)

for _ in range(M):
    x = pq.get()
    y = pq.get()
    pq.put(x + y)
    pq.put(x + y)

sum = 0
while pq.qsize() != 0:
    sum += pq.get()

print(sum)