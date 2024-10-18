import sys
from queue import PriorityQueue

input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))

pq = PriorityQueue()
for i in range(N):
    pq.put((A[i], i))


M = int(input())
for _ in range(M):
    query = input().split()

    if query[0] == '1':
        i = int(query[1]) - 1
        v = int(query[2])
        A[i] = v
        pq.put((A[i], i))

    if query[0] == '2':
        while True:
            v, i = pq.get()

            if A[i] != v:
                continue

            print(i + 1)
            pq.put((v, i))
            break