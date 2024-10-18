N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

B = [0] * M
pos1 = 0
while True:
    B[0] += A[pos1]
    pos1 += 1

    pos2 = 1
    while pos1 < N and pos2 < M:
        B[pos2] += A[pos1]
        pos1 += 1
        if B[pos2] == B[0]:
            pos2 += 1

    if pos1 == N:
        break

print(B[0])