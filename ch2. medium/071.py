R, C, K = map(int, input().split())
B = [input() for _ in range(R)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

answer = 0
def dfs(r, c, k, used):
    if k == 0:
        if r == 0 and c == C - 1:
            global answer
            answer += 1
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or R <= nr or nc < 0 or C <= nc:
            continue
        if B[nr][nc] == 'T':
            continue
        if (nr, nc) not in used:
            used.append((nr, nc))
            dfs(nr, nc, k - 1, used)
            used.pop(-1)

dfs(R - 1, 0, K - 1, [(R - 1, 0)])
print(answer)