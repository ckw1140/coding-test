N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

cache = [[-1] * (2 ** N) for _ in range(N)]
def dp(x, mask):
    if cache[x][mask] != -1:
        return cache[x][mask]

    if x == 0:
        for i in range(N):
            if mask == (2 ** i):
                cache[x][mask] = D[x][i]
                return D[x][i]

    ret = 1e9
    for i in range(N):
        if mask & (2 ** i) != 0:
            ret = min(ret, D[x][i] + dp(x - 1, mask - (2 ** i)))

    cache[x][mask] = ret
    return ret


print(dp(N - 1, 2 ** N - 1))