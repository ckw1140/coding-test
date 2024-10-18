N = int(input())
A = list(map(int, input().split()))

def dfs(a, w):
    if len(a) == 2:
        return w

    ret = 0
    for i in range(1, len(a) - 1):
        v = dfs(a[:i] + a[i + 1:], w + a[i - 1] * a[i + 1])
        ret = max(ret, v)

    return ret

print(dfs(A, 0))