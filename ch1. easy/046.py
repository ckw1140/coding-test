N = input()
count = 0

def dfs(n):
    ret = 0

    if n == N:
        return 1

    if N.find(n) == -1:
        return 0

    for i in range(10):
        left = str(i) + n
        right = n + str(i)
        if left == right:
            ret += dfs(left)
        else:
            ret += dfs(left)
            ret += dfs(right)
    
    return ret

print(dfs(""))