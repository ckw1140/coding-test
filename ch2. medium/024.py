N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

max_plus = -1e9
min_plus = 1e9
for i in range(N):
    max_plus = max(max_plus, P[i][0] + P[i][1])
    min_plus = min(min_plus, P[i][0] + P[i][1])

max_minus = -1e9
min_minus = 1e9
for i in range(N):
    max_minus = max(max_minus, P[i][1] - P[i][0])
    min_minus = min(min_minus, P[i][1] - P[i][0])

print(max(max_plus - min_plus, max_minus - min_minus))