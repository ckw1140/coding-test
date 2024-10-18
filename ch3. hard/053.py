N, M = map(int, input().split())
C = [-1] * N

for i in range(M):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1

    for j in range(l, r + 1):
        C[j] = i

C = list(set(C) - {-1})
print(2 ** (len(C)))