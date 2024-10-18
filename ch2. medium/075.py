import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    adj[a].append(b)

visit = [[False] * N for _ in range(N)]
for i in range(N):
    queue = deque()
    queue.append(i)
    visit[i][i] = True

    while len(queue) != 0:
        u = queue.popleft()

        for v in adj[u]:
            if not visit[i][v]:
                queue.append(v)
                visit[i][v] = True

S = int(input())
for _ in range(S):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if visit[a][b]:
        print("-1")
    elif visit[b][a]:
        print("1")
    else:
        print("0")