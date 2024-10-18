N, M = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(M)]

C.sort(reverse=True)
cost = 0
for i in range(M - 1):
    if C[i][0] < N:
        cost += N - C[i][0]

print(cost)