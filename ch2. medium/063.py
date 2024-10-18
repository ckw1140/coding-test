from queue import PriorityQueue

N, K, A, B = map(int, input().split())

N //= A

pq = PriorityQueue()
for _ in range(N):
    pq.put(K)

count = 0
zero = 0
while True:
    x = pq.get()
    if x == zero:
        break

    x += B
    pq.put(x)
    zero += 1
    count += 1

print(count)