T, W = map(int, input().split())
A = [int(input()) - 1 for _ in range(T)]

cache = [
    [[-1] * (W + 1) for _ in range(2)] for _ in range(T + 1)
]
def dp(t, p, w):
    if cache[t][p][w] != -1:
        return cache[t][p][w]

    if t == T:
        cache[t][p][w] = 0
        return 0

    ret = 0
    if A[t] == p:
        ret = max(ret, dp(t + 1, p, w) + 1)
        if w > 0:
            ret = max(ret, dp(t + 1, 1 - p, w - 1))
    else:
        ret = max(ret, dp(t + 1, p, w))
        if w > 0:
            ret = max(ret, dp(t + 1, 1 - p, w - 1) + 1)

    cache[t][p][w] = ret
    return ret


print(dp(0, 0, W))