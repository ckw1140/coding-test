N, P, Q, X, Y = map(int, input().split())


cache = {}
def dp(n):
    if n <= 0:
        return 1
    if n in cache:
        return cache[n]

    ret = dp(n // P - X) + dp(n // Q - Y)
    cache[n] = ret
    return ret

print(dp(N))