N = int(input())

B = [[0] * 21 for _ in range(21)]

def is_five(r, c, d):
    if B[r][c] == 0:
        return False
    if d == 0:
        return (
            r + 5 < 21
            and B[r - 1][c] != B[r][c]
            and B[r + 1][c] == B[r][c]
            and B[r + 2][c] == B[r][c]
            and B[r + 3][c] == B[r][c]
            and B[r + 4][c] == B[r][c]
            and B[r + 5][c] != B[r][c]
        )
    if d == 1:
        return (
            c + 5 < 21
            and B[r][c - 1] != B[r][c]
            and B[r][c + 1] == B[r][c]
            and B[r][c + 2] == B[r][c]
            and B[r][c + 3] == B[r][c]
            and B[r][c + 4] == B[r][c]
            and B[r][c + 5] != B[r][c]
        )
    if d == 2:
        return (
            r + 5 < 21
            and c + 5 < 21
            and B[r - 1][c - 1] != B[r][c]
            and B[r + 1][c + 1] == B[r][c]
            and B[r + 2][c + 2] == B[r][c]
            and B[r + 3][c + 3] == B[r][c]
            and B[r + 4][c + 4] == B[r][c]
            and B[r + 5][c + 5] != B[r][c]
        )
    if d == 3:
        return (
            r + 5 < 21
            and c - 5 >= 0
            and B[r - 1][c + 1] != B[r][c]
            and B[r + 1][c - 1] == B[r][c]
            and B[r + 2][c - 2] == B[r][c]
            and B[r + 3][c - 3] == B[r][c]
            and B[r + 4][c - 4] == B[r][c]
            and B[r + 5][c - 5] != B[r][c]
        )

answer = 1e9
for i in range(N):
    r, c = map(int, input().split())
    B[r][c] = 1 if i % 2 == 0 else 2

    for j in range(1, 20):
        for k in range(1, 20):
            for d in range(4):
                if is_five(j, k, d):
                    answer = min(answer, i)

if answer == 1e9:
    print(-1)
else:
    print(answer + 1)