T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    K = int(input())
    C = list(map(int, input().split()))

    lucky = []
    for i in range(N):
        for j in range(M):
            for k in range(K):
                sum = A[i] + B[j] + C[k]
                good = True
                while sum > 0:
                    if sum % 10 not in [5, 8]:
                        good = False
                        break
                    sum //= 10

                if good:
                    lucky.append(A[i] + B[j] + C[k])

    print(len(list(set(lucky))))