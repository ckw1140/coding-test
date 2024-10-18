N, M, C = map(int, input().split())
W = list(map(int, input().split()))

cache = [
    [[-1] * 2**N for _ in range(C + 1)] for _ in range(M)
]
def dp(m, c, mask):
    if cache[m][c][mask] != -1:
        return cache[m][c][mask]

    ret = 0
    if m > 0:
        ret = max(ret, dp(m - 1, 0, mask))

    for i in range(N):
        if mask & (2 ** i) != 0:
            if c + W[i] <= C:
                ret = max(
                    ret,
                    1 + dp(m, c + W[i], mask - (2**i)),
                )

    cache[m][c][mask] = ret
    return ret

print(dp(M - 1, 0, 2**N - 1))