import sys
from queue import PriorityQueue

input = sys.stdin.readline

N, K = map(int, input().split())

J = [tuple(map(int, input().split())) for _ in range(N)]
B = [int(input()) for _ in range(K)]

J.sort()
B.sort()

pq = PriorityQueue()

answer = 0
pos = 0
for i in range(K):
    while pos < N and J[pos][0] <= B[i]:
        pq.put(-J[pos][1])
        pos += 1

    if pq.qsize() > 0:
        answer += -pq.get()

print(answer)