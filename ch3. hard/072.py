N, M, D = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

def simulation(A, c1, c2, c3):
    count = 0
    for _ in range(N):
        kill1, kill2, kill3 = (-1, -1), (-1, -1), (-1, -1)
        for j in range(M):
            for i in range(N):
                if A[i][j] == 1:
                    if abs(i - N) + abs(j - c1) <= D:
                        if kill1 == (-1, -1):
                            kill1 = (i, j)
                        elif abs(i - N) + abs(j - c1) < abs(kill1[0] - N) + abs(kill1[1] - c1):
                            kill1 = (i, j)
                    if abs(i - N) + abs(j - c2) <= D:
                        if kill2 == (-1, -1):
                            kill2 = (i, j)
                        elif abs(i - N) + abs(j - c2) < abs(kill2[0] - N) + abs(kill2[1] - c2):
                            kill2 = (i, j)
                    if abs(i - N) + abs(j - c3) <= D:
                        if kill3 == (-1, -1):
                            kill3 = (i, j)
                        elif abs(i - N) + abs(j - c3) < abs(kill3[0] - N) + abs(kill3[1] - c3):
                            kill3 = (i, j)

        if kill1 != (-1, -1):
            count += A[kill1[0]][kill1[1]]
            A[kill1[0]][kill1[1]] = 0
        if kill2 != (-1, -1):
            count += A[kill2[0]][kill2[1]]
            A[kill2[0]][kill2[1]] = 0
        if kill3 != (-1, -1):
            count += A[kill3[0]][kill3[1]]
            A[kill3[0]][kill3[1]] = 0

        for i in range(N - 1, 0, -1):
            A[i] = A[i - 1].copy()
        A[0] = [0] * M

    return count

answer = 0
for i in range(M):
    for j in range(i + 1, M):
        for k in range(j + 1, M):
            A = [B[i].copy() for i in range(N)]
            answer = max(answer, simulation(A, i, j, k))

print(answer)