N = int(input())
S = [input() for _ in range(N)]

cache = [[-1] * (2 ** N) for _ in range(N)]
def dp(last, mask):
    if cache[last][mask] != -1:
        return cache[last][mask]

    ret = len(S[last])
    for i in range(N):
        if i == last:
            continue
        if mask & (2**i) != 0 and S[i][-1] == S[last][0]:
            ret = max(ret, len(S[last]) + dp(i, mask - (2 ** last)))

    cache[last][mask] = ret
    return ret

answer = 0
for i in range(N):
    answer = max(answer, dp(i, 2 ** N - 1))
print(answer)
