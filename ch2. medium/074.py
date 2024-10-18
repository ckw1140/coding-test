N = int(input())
F = [input() for _ in range(N)]

max_count = 0
for i in range(N):
    f2 = set()
    for j in range(N):
        if F[i][j] == 'Y':
            f2.add(j)
            for k in range(N):
                if F[j][k] == 'Y' and k != i:
                    f2.add(k)

    max_count = max(max_count, len(f2))

print(max_count)