import sys
from collections import deque

input = sys.stdin.readline

testcase = 1
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    adj = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1

        adj[a].append(b)
        adj[b].append(a)

    visit = [False] * N
    queue = deque()

    num_trees = 0
    for i in range(N):
        if not visit[i]:
            queue.append(i)
            visit[i] = True

            num_nodes = 1
            num_edges = 0

            while len(queue) != 0:
                u = queue.popleft()

                for v in adj[u]:
                    num_edges += 1
                    if not visit[v]:
                        queue.append(v)
                        visit[v] = True
                        num_nodes += 1

            num_edges /= 2
            if num_edges == num_nodes - 1:
                num_trees += 1

    print(f"Case {testcase}:", end=" ")
    if num_trees == 0:
        print("No trees.")
    elif num_trees == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {num_trees} trees.")

    testcase += 1
