from itertools import combinations


N, M = map(int, input().split())
A = [list(map(int, input().split()))[1:] for _ in range(M)]
A = [set(a) for a in A]

answer = -1
for n in range(1, M + 1):
    found = False
    for combination in combinations(A, n):
        U = set()
        for a in combination:
            U = U | a

        if len(list(U)) == N:
            found = True
            break

    if found:
        answer = n
        break

print(answer)