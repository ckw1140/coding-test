import sys
from collections import deque


T = int(input())

for _ in range(T):
    N = int(input())

    if N == 1:
        print(1)
        continue

    visit = [False] * N
    prev = [-1] * N
    queue = deque()

    queue.append(1)
    visit[1] = True
    
    while len(queue) != 0:
        u = queue.popleft()
        if u == 0:
            break

        if not visit[(10 * u) % N]:
            queue.append((10 * u) % N)
            visit[(10 * u) % N] = True
            prev[(10 * u) % N] = u
        if not visit[(10 * u + 1) % N]:
            queue.append((10 * u + 1) % N)
            visit[(10 * u + 1) % N] = True
            prev[(10 * u + 1) % N] = u


    answer = []
    u = 0
    while u != 1:
        if (10 * prev[u]) % N == u:
            answer.append('0')
        else:
            answer.append('1')
        u = prev[u]
    answer.append('1')
    print("".join(answer[::-1]))