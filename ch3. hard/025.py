N = int(input())
A = list(map(int, input().split()))

if N == 3:
    if A[0] + A[2] > A[1]:
        print(-1)
    else:
        print(A[1] - A[0] - A[2])
else:
    even = 0
    odd = 0
    for i in range(N):
        if i % 2 == 0:
            even += A[i]
        else:
            odd += A[i]

    print(abs(even - odd))