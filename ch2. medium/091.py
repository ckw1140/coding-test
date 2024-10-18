R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]

def dfs(r, c):
    B[r][c] = 'x'
    if c == C - 1:
        return True
    if r - 1 >= 0 and B[r - 1][c + 1] == '.' and dfs(r - 1, c + 1):
        return True
    if B[r][c + 1] == '.' and dfs(r, c + 1):
        return True
    if r + 1 < R and B[r + 1][c + 1] == '.' and dfs(r + 1, c + 1):
        return True
    return False

answer = 0
for i in range(R):
    if dfs(i, 0):
        answer += 1

print(answer)