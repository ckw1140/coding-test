import sys
from collections import deque

input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    count = [0] * N

    for _ in range(K):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        adj[x].append(y)
        count[y] += 1

    W = int(input())
    W -= 1

    finish = [0] * N
    queue = deque()
    for i in range(N):
        if count[i] == 0:
            queue.append(i)
            finish[i] = D[i]
    
    while len(queue) != 0:
        u = queue.popleft()

        for v in adj[u]:
            count[v] -= 1
            finish[v] = max(finish[v], finish[u] + D[v])
            if count[v] == 0:
                queue.append(v)

    print(finish[W])