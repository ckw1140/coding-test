N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
S = input()
P = int(input())

cache = [-1] * (2 ** 16)
def dp(mask):
    if cache[mask] != -1:
        return cache[mask]

    count = 0
    for i in range(N):
        if mask & (2 ** i) != 0:
            count += 1

    if count >= P:
        cache[mask] = 0
        return 0

    ret = 1e9
    for i in range(N):
        if mask & (2 ** i) != 0:
            for j in range(N):
                if mask & (2 ** j) == 0:
                    ret = min(ret, A[i][j] + dp(mask + (2 ** j)))

    cache[mask] = ret
    return ret

init_mask = 0
for i in range(N):
    if S[i] == 'Y':
        init_mask += (2 ** i)

answer = dp(init_mask)
if answer == 1e9:
    print(-1)
else:
    print(answer)