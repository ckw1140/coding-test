N = int(input())
dist = [list(map(int, input().split())) for _ in range(N)]
need = [[True] * N for _ in range(N)]

impossible = False
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or j == k:
                continue
            if dist[i][j] + dist[j][k] == dist[i][k]:
                need[i][k] = False
            elif dist[i][j] + dist[j][k] < dist[i][k]:
                impossible = True
                break


if impossible:
    print(-1)
else:
    answer = 0
    for i in range(N):
        for j in range(i + 1, N):
            if need[i][j]:
                answer += dist[i][j]

    print(answer)