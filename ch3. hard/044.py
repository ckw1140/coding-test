N = int(input())
S = "아점저" * N

cache = [[-1] * 3 * N for _ in range(3 * N)]
def dp(l, r):
    if cache[l][r] != -1:
        return cache[l][r]

    if l == r:
        cache[l][r] = 1
        return 1

    ret = 0
    if (r - l + 1) % 3 == 2:
        # 점심 약 먹을 타이밍
        if S[l] == '점':
            ret += dp(l + 1, r)
        if S[r] == '점':
            ret += dp(l, r - 1)
    else:
        if S[l] != '점':
            ret += dp(l + 1, r)
        if S[r] != '점':
            ret += dp(l, r - 1)

    cache[l][r] = ret
    return ret

print(dp(0, 3 * N - 1))