from collections import deque

N = int(input())
F = [input() for _ in range(N)]

max_count = 0
for i in range(N):
    visit = [False] * N
    dist = [-1] * N
    queue = deque()

    queue.append(i)
    visit[i] = True
    dist[i] = 0
    
    while len(queue) != 0:
        u = queue.popleft()

        for v in range(N):
            if F[u][v] == 'Y' and not visit[v]:
                queue.append(v)
                visit[v] = True
                dist[v] = dist[u] + 1

    count = 0
    for j in range(N):
        if j != i and dist[j] != -1 and dist[j] <= 2:
            count += 1

    max_count = max(max_count, count)

print(max_count)