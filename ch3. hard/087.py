N = int(input())
A = list(map(int, input().split()))

if N < 3:
    print(N)
else:
    A.sort()
    answer = 2
    for i in range(N):
        for j in range(i + 2, N):
            if A[i] + A[i + 1] > A[j]:
                answer = max(answer, j - i + 1)

    print(answer)