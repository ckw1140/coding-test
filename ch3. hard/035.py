from queue import PriorityQueue

N, M = map(int, input().split())
B = [input() for _ in range(N)]
adj = {}
count = {}

check = set()
impossible = False
for i in range(N):
    for j in range(M):
        if B[i][j] == '.':
            continue

        if B[i][j] in check:
            continue
        
        check.add(B[i][j])
        adj[B[i][j]] = []
        if B[i][j] not in count:
            count[B[i][j]] = 0

        rs = []
        cs = []
        for r in range(N):
            for c in range(M):
                if B[r][c] == B[i][j]:
                    rs.append(r)
                    cs.append(c)

        min_r = min(rs)
        max_r = max(rs)
        min_c = min(cs)
        max_c = max(cs)

        for r in range(min_r, max_r + 1):
            for c in range(min_c, max_c + 1):
                if B[r][c] != B[i][j]:
                    if B[r][c] == '.':
                        impossible = True
                        break
                    adj[B[i][j]].append(B[r][c])
                    if B[r][c] not in count:
                        count[B[r][c]] = 0
                    count[B[r][c]] += 1


if impossible:
    print(-1)
else:
    pq = PriorityQueue()
    for k, v in count.items():
        if v == 0:
            pq.put(k)

    answer = []
    while pq.qsize() != 0:
        u = pq.get()
        answer.append(u)

        for v in adj[u]:
            count[v] -= 1
            if count[v] == 0:
                pq.put(v)

    if len(answer) != len(adj):
        print(-1)
    else:
        print("".join(answer))