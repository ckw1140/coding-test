N, M = map(int, input().split())
adj = [set() for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())

    adj[a].add(b)
    adj[b].add(a)

found = False
for b in range(N):
    for d in range(b + 1, N):
        inter = adj[b] & adj[d]
        diff_b = adj[b] - adj[d] - set([d])
        diff_d = adj[d] - adj[b] - set([b])

        if len(inter) >= 3:
            found = True
            break
        elif len(inter) == 2:
            if len(diff_b) > 0 or len(diff_d) > 0:
                found = True
                break
        elif len(inter) == 1:
            if len(diff_b) > 0 and len(diff_d) > 0:
                found = True
                break

if found:
    print(1)
else:
    print(0)