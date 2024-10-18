from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
A = [x - 1 for x in A]

count = [0] * 3
for x in A:
    count[x] += 1

answer = 1e9
for permutation in permutations([0, 1, 2], 3):
    B = []
    for x in permutation:
        B += [x] * count[x]
    

    wrong = [[0] * 3 for _ in range(3)]
    for i in range(N):
        if A[i] != B[i]:
            wrong[A[i]][B[i]] += 1

    num_changes = 0
    remain = 0
    for i in range(3):
        for j in range(i + 1, 3):
            tmp = min(wrong[i][j], wrong[j][i])
            num_changes += tmp
            wrong[i][j] -= tmp
            wrong[j][i] -= tmp
            remain = max(wrong[i][j], wrong[j][i])

    num_changes += remain * 2
    answer = min(answer, num_changes)

print(answer)