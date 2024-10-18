from collections import deque

S, T = map(int, input().split())

visit = set()
path = {}
queue = deque()

queue.append(S)
visit.add(S)
path[S] = ""

while len(queue) != 0:
    u = queue.popleft()

    if u * u <= 1e9 and u * u not in visit:
        queue.append(u * u)
        visit.add(u * u)
        path[u * u] = path[u] + "*"
    if u + u <= 1e9 and u + u not in visit:
        queue.append(u + u)
        visit.add(u + u)
        path[u + u] = path[u] + "+"
    if u / u <= 1e9 and u / u not in visit:
        queue.append(u / u)
        visit.add(u / u)
        path[u / u] = path[u] + "/"

if S == T:
    print(0)
elif T in path:
    print(path[T])
else:
    print("-1")