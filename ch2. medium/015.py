from collections import deque

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
adj = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)


visit = [False] * N
queue = deque()

total = 0
for i in range(N):
    if visit[i]:
        continue

    queue.append(i)
    visit[i] = True
    min_cost = A[i]

    while len(queue) != 0:
        u = queue.popleft()

        for v in adj[u]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True
                min_cost = min(min_cost, A[v])

    total += min_cost

if total <= K:
    print(total)
else:
    print("Oh no")