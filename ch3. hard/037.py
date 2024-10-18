N = int(input())
mod = 10 ** 9

cache = [
    [[-1] * (2 ** 10) for _ in range(10)]
    for _ in range(N + 1)
]
def dp(n, d, mask):
    if cache[n][d][mask] != -1:
        return cache[n][d][mask]

    if n == 1:
        if d == 0:
            ret = 0
        elif mask != (2 ** d):
            ret = 0
        else:
            ret = 1
        cache[n][d][mask] = ret
        return ret

    ret = 0
    if 0 <= d - 1 and mask & (2 ** (d - 1)) != 0:
        ret += dp(n - 1, d - 1, mask)
        ret += dp(n - 1, d - 1, mask - (2 ** d))
        ret %= mod
    if 10 > d + 1 and mask & (2 ** (d + 1)) != 0:
        ret += dp(n - 1, d + 1, mask)
        ret += dp(n - 1, d + 1, mask - (2 ** d))
        ret %= mod

    cache[n][d][mask] = ret
    return ret

answer = 0
for i in range(10):
    answer += dp(N, i, (2 ** 10) - 1)
    answer %= mod

print(answer)