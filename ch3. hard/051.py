from collections import deque

N, K = map(int, input().split())
S = input()

H = 0
T = 0
for s in S:
    if s == 'H':
        H += 1
    else:
        T += 1

visit = set()
dist = {}
queue = deque()

queue.append((H, T))
visit.add((H, T))
dist[(H, T)] = 0

while len(queue) != 0:
    h, t = queue.popleft()

    for i in range(K + 1):
        if h < i or t < K - i:
            continue
        nh = h - i + K - i
        nt = t - K + i + i

        if (nh, nt) not in visit:
            queue.append((nh, nt))
            visit.add((nh, nt))
            dist[(nh, nt)] = dist[(h, t)] + 1

if (0, N) in visit:
    print(dist[(0, N)])
else:
    print(-1)