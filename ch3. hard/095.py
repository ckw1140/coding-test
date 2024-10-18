N = int(input())
P = list(map(int, input().split()))

D = [1e9] * N
D[0] = P[0]
for i in range(1, N):
    D[i] = min(D[i - 1], P[i])

answer = 0
for i in range(N):
    answer = max(answer, P[i] - D[i])

print(answer)