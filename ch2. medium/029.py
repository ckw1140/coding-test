from collections import deque

N = int(input())
M = int(input())
adj = [[] for _ in range(N)]
count = [0] * N

for _ in range(M):
    x, y, k = map(int, input().split())
    x -= 1
    y -= 1

    adj[x].append((y, k))
    count[y] += 1

answer = [0] * N
answer[N - 1] = 1

queue = deque()
queue.append(N - 1)

while len(queue) != 0:
    u = queue.popleft()

    for v, w in adj[u]:
        answer[v] += answer[u] * w
        count[v] -= 1
        if count[v] == 0:
            queue.append(v)

for i in range(N):
    if len(adj[i]) == 0:
        print(i + 1, answer[i])