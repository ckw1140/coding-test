import sys
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())

    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)

Q = int(input())

for _ in range(Q):
    t, k = map(int, input().split())

    if t == 1:
        if len(adj[k - 1]) == 1:
            print("no")
        else:
            print("yes")
    if t == 2:
        print("yes")