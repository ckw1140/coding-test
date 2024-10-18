N, R, G, B = map(int, input().split())

fact = [0] * (N + 1)
fact[0] = 1
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i


cache = [[[[-1] * 101 for _ in range(101)] for _ in range(101)] for _ in range(11)]

def dp(n, r, g, b):
    if cache[n][r][g][b] != -1:
        return cache[n][r][g][b]

    if n == 0:
        cache[n][r][g][b] = 1
        return 1

    ret = 0
    if r >= n:
        ret += dp(n - 1, r - n, g, b)
    if g >= n:
        ret += dp(n - 1, r, g - n, b)
    if b >= n:
        ret += dp(n - 1, r, g, b - n)

    if n % 2 == 0:
        if r >= n // 2 and g >= n // 2:
            ret += dp(n - 1, r - n // 2, g - n // 2, b) * fact[n] // fact[n // 2] ** 2

        if g >= n // 2 and b >= n // 2:
            ret += dp(n - 1, r, g - n // 2, b - n // 2) * fact[n] // fact[n // 2] ** 2

        if b >= n // 2 and r >= n // 2:
            ret += dp(n - 1, r - n // 2, g, b - n // 2) * fact[n] // fact[n // 2] ** 2

    if n % 3 == 0:
        if r >= n // 3 and g >= n // 3 and b >= n // 3:
            ret += dp(n - 1, r - n // 3, g - n // 3, b - n // 3) * fact[n] // fact[n // 3] ** 3

    cache[n][r][g][b] = ret
    return ret


print(dp(N, R, G, B))