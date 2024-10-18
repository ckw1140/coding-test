import sys
sys.setrecursionlimit(123458)


N = int(input())
A = [0] * N
child = [[] for _ in range(N)]

for i in range(1, N):
    t, a, p = input().split()
    a = int(a)
    p = int(p) - 1
    if t == 'S':
        A[i] = a
    else:
        A[i] = -a
    
    child[p].append(i)

D = [0] * N

def dfs(u):
    D[u] = A[u]
    for v in child[u]:
        dfs(v)
        D[u] += D[v]

    if D[u] < 0:
        D[u] = 0

dfs(0)
print(D[0])