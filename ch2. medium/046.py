W, H, N = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N - 1):
    x1, y1 = P[i]
    x2, y2 = P[i + 1]

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    if y1 > y2:
        answer += abs(x1 - x2) + abs(y1 - y2)
    else:
        answer += max(abs(x1 - x2), abs(y1 - y2))

print(answer)