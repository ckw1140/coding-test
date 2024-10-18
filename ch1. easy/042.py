N, K = map(int, input().split())
A = list(map(int, input().split()))
D = [A[i + 1] - A[i] for i in range(N - 1)]
D.sort(reverse=True)

answer = A[N - 1] - A[0]
for i in range(K - 1):
    answer -= D[i]

print(answer)