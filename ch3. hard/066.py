N, K = map(int, input().split())

cache = [
    [
        [[-1] * (K + 1) for _ in range(N + 1)]
        for _ in range(N + 1)
    ]
    for _ in range(N + 1)
]
def dp(a, b, c, k):
    if cache[a][b][c][k] != -1:
        return cache[a][b][c][k]

    if a == 0 and b == 0 and c == 0:
        cache[a][b][c][k] = k == 0
        return k == 0

    ret = 0
    if a > 0 and dp(a - 1, b, c, k):
        ret = 1
    if b > 0 and k >= a and dp(a, b - 1, c, k - a):
        ret = 1
    if c > 0 and k >= a + b and dp(a, b, c - 1, k - a - b):
        ret = 1

    cache[a][b][c][k] = ret
    return ret


def solve(a, b, c, k):
    if a == 0 and b == 0 and c == 0:
        return ""

    if a > 0 and dp(a - 1, b, c, k):
        return solve(a - 1, b, c, k) + "A"

    if b > 0 and dp(a, b - 1, c, k - a):
        return solve(a, b - 1, c, k - a) + "B"

    if c > 0 and dp(a, b, c - 1, k - a - b):
        return solve(a, b, c - 1, k - a - b) + "C"

found = False
for a in range(N + 1):
    for b in range(N + 1 - a):
        c = N - a - b

        if dp(a, b, c, K):
            found = True
            print(solve(a, b, c, K))
            break

    if found:
        break

if not found:
    print(-1)