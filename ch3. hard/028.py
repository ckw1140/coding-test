from queue import PriorityQueue

N = int(input())
P = list(map(int, input().split()))
A = list(map(int, input().split()))

child = [[] for _ in range(N)]
for i in range(N - 1):
    child[P[i] - 1].append(i + 1)

pq = PriorityQueue()
pq.put((-A[0], 0))
answer = 0

for _ in range(N):
    x, u = pq.get()
    answer += -x

    print(answer)

    for v in child[u]:
        pq.put((-A[v], v))