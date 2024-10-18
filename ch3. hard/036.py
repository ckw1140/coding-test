N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()

answer = 0
for i in range(1, N - 1):
    min_avg = A[0] + A[i] + A[i + 1]
    max_avg = A[i - 1] + A[i] + A[N - 1]

    answer = max(answer, abs(min_avg - 3 * A[i]))
    answer = max(answer, abs(max_avg - 3 * A[i]))

print(answer)