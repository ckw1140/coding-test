N = int(input())
A = list(map(int, input().split()))
B = [(A[i], i) for i in range(N)]
B.sort(reverse=True)
total = sum(A)
MAX = 100001

D = [[False] * MAX for _ in range(N)]
D[0][0] = True
D[0][B[0][0]] = True

clean = B[0][0] if B[0][0] > total // 2 else -1
for i in range(1, N):
    for j in range(total // 2 + 1 - B[i][0], total // 2 + 1):
        if D[i - 1][j]:
            clean = max(clean, j + B[i][0])

    for j in range(MAX):
        if D[i - 1][j]:
            D[i][j] = True
            D[i][j + B[i][0]] = True

answer = []
while clean != 0:
    for i in range(N):
        if D[i][clean]:
            clean -= B[i][0]
            answer.append(B[i][1] + 1)
            break

answer.sort()
print(len(answer))
print(*answer)