N, X = map(int, input().split())

D = [0] * (N + 1)
E = [0] * (N + 1)
D[0] = 1
E[0] = 1
for i in range(1, N + 1):
    D[i] = 2 * D[i - 1] + 3
    E[i] = 2 * E[i - 1] + 1

def solve(n, x):
    if D[n] < x:
        x = D[n]
    if n == 0:
        return x
    if x == 0:
        return 0
    
    if x <= 1 + D[n - 1]:
        return solve(n - 1, x - 1)
    else:
        return E[n - 1] + 1 + solve(n - 1, x - 2 - D[n - 1])


print(solve(N, X))