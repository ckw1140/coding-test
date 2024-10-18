from queue import PriorityQueue

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    A[i].sort()

pq = PriorityQueue()
pos = [0] * N
max_val = 0
for i in range(N):
    pq.put((A[i][0], i))
    max_val = max(max_val, A[i][0])

answer = 1e9
while True:
    min_val, id = pq.get()
    answer = min(answer, max_val - min_val)

    pos[id] += 1
    if pos[id] >= M:
        break
    pq.put((A[id][pos[id]], id))
    max_val = max(max_val, A[id][pos[id]])

print(answer)